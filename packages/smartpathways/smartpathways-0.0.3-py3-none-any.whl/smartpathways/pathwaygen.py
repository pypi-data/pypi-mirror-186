from bson import ObjectId
import numpy as np
import pymongo
import random


class mapGenerator:
    __dbConnectionString = "localhost:27017"
    __client = pymongo.MongoClient(host=__dbConnectionString, directConnection=True)

    # constructor
    def __init__(self, assessmentProblemId):
        self.assessProblemId = assessmentProblemId

    # instance methods
    def __getPathwayRankListByProblem(self, assessmentProblemId):
        docs = list(self.__client.get_database("metric").get_collection("pathwayrankbyproblem").find({"problemId":assessmentProblemId}, {"_id":0, "pathwayrankList":1}))
        return docs[0]    

    def __getAssessmentId(self, assessmentProblemId):
        docs = list(self.__client.get_database("content").get_collection("problems").find({"_id":assessmentProblemId}, {"_id":0, "folderId":1}))
        return docs[0]["folderId"] 

    def __getSectionId(self, assessmentId):
        docs = list(self.__client.get_database("content").get_collection("folders").find({"_id":assessmentId}, {"_id":0, "parentId":1}))
        return docs[0]["parentId"] 

    def __getExerciseId(self, sectionId):
        docs = list(self.__client.get_database("content").get_collection("folders").find({"parentId":sectionId, "type":"EXERCISE"}, {"_id":1}))
        return docs[0]["_id"] 

    def __getExerciseProblemIDs(self, assessmentProblemId):
        exerciseId = self.__getExerciseId(self.__getSectionId(self.__getAssessmentId(assessmentProblemId = assessmentProblemId)))
        docs = list(self.__client.get_database("content").get_collection("problems").find({"folderId":exerciseId, "deleted":False}, {"_id":1}))
        return docs

    def __calcNumberExerciseProblems(self, pathwayAssignCount, threshold, pathwayCount, exerciseCount, poolLen):

        # Next 2 values should add up to less than poolLength
        # We should always have a minimum of 2 exercise questions, and 2 pathway questions in our pool
        minExerciseQs = 2
        maxExerciseQs = 5

        assert ((minExerciseQs + maxExerciseQs) < poolLen)

        if ((pathwayCount + exerciseCount) >= poolLen):
            if (pathwayAssignCount <= threshold):
                theoNumExercQs = int(np.round(((maxExerciseQs - minExerciseQs)/(0 - threshold)*pathwayAssignCount + maxExerciseQs), 0))
                theoNumPathQs = poolLen - theoNumExercQs
                
            else:
                theoNumExercQs = minExerciseQs
                theoNumPathQs = poolLen - theoNumExercQs
            

            if (theoNumPathQs > pathwayCount):
                numPathQs = pathwayCount
                numExercQs = poolLen - numPathQs
            elif (theoNumExercQs > exerciseCount):
                numExercQs = exerciseCount
                numPathQs = poolLen - numExercQs
            else:
                numExercQs = theoNumExercQs
                numPathQs = theoNumPathQs

        else:
            poolLen = (pathwayCount + exerciseCount)
            numExercQs = exerciseCount
            numPathQs = pathwayCount

        return numExercQs, numPathQs, poolLen

    def __getRandomExerciseProbs(self, countMissing, exerciseProbIds, existingProbs):
        probsToAdd = []
        probPool = existingProbs.copy()

        for count in range(0, countMissing):
            exerciseProblemIdsUnique = []

            # test if exercise questions are already in problem pool
            for item in exerciseProbIds:
                if (probPool.count(item) == 0):
                    exerciseProblemIdsUnique.append(item)
            
            randomExerciseQ = exerciseProblemIdsUnique[np.random.randint(0, len(exerciseProblemIdsUnique))]
            probPool.append(randomExerciseQ)
            probsToAdd.append(randomExerciseQ)

        return probsToAdd

    def __calcAdjustedSuccessRatio(self, assigned, correct):
        ###################### Fitting parameters ######################
        rootOrder = 2
        alpha = 0.7   # 0 < alpha < 1
        dummySuccess = 0.5 # Success ratio if pathway has never been assigned before, or if pathway has low assignments and a 0% success ratio
        ################################################################

        if (assigned==0):
            result = dummySuccess
        else:
            observedRatio = correct/assigned

            if (observedRatio == 0):
                result = dummySuccess/(assigned**(1/rootOrder))
            else:
                result = observedRatio - alpha*observedRatio/(assigned**(1/rootOrder))
        return result 

    def __getTopPathwayProblems(self, rankList, countProblems):
        ## Calculate all pathway success ratios
        pathwaySuccessRatiosAssigned = []
        pathwaySuccessRatiosUnassigned = []

        for pathway in rankList:
            globalAssigned = pathway["globalAssigned"]
            globalSuccess = pathway["globalSuccess"]
            
            adjSuccessRatio = self.__calcAdjustedSuccessRatio(correct=globalSuccess, assigned=globalAssigned)

            if (globalAssigned > 0): # Test if it is the first time pathway is being assigned
                pathwaySuccessRatiosAssigned += [[pathway["pathwayId"], adjSuccessRatio]]
                
            else:
                pathwaySuccessRatiosUnassigned += [[pathway["pathwayId"], adjSuccessRatio]]
        
        ## Use all pathways in rankList
        if (countProblems == len(rankList)):
            return pathwaySuccessRatiosAssigned + pathwaySuccessRatiosUnassigned

        ## Pick some (top) pathways from rankList 
        else:
            #No pathways have been assigned <=> all picked randomly
            if (len(pathwaySuccessRatiosUnassigned) == len(rankList)): 
                indexes = random.sample(range(0, len(rankList)), countProblems)
                temp = []
                for index in indexes:
                    temp.append(pathwaySuccessRatiosUnassigned[index])

                return temp
            
            # Some/all pathways assigned - but 1 pathway should always be randomly assigned, to allow new content to become pathway
            else: 
                pathwaySuccessRatiosSorted = sorted(pathwaySuccessRatiosAssigned, key=lambda x: x[1], reverse=True)
                
                toChooseFromUnassigned = np.max([countProblems - len(pathwaySuccessRatiosSorted), 0])
                
                # Can choose from either unassigned or unselected list - but enough problems exist to allow us to only select from unselected list
                if (toChooseFromUnassigned == 0):
                    countProblemsAssigned = countProblems - 1

                    mergedList, unselectedPathways = self.__getPathwaysAroundSlicePoint(pathwaySuccessRatiosSorted, countProblemsAssigned - 1)
                    
                    # No unassigned pathways exist <=> pick 1 random pathway (which hasnt already been chosen) from assigned list
                    if (len(pathwaySuccessRatiosUnassigned) == 0): 
                        unselectedPathways = pathwaySuccessRatiosSorted[countProblems-1:]
                        index = np.random.randint(0,len(unselectedPathways))
                        mergedList.extend(unselectedPathways[index])
                    
                    # Unassigned pathways still exist <=> pick 1 random pathway from unassigned list or unselected list
                    else: 
                        randomNum = np.random.randint(0,2)
                        
                        # Add from unselected list
                        if (randomNum == 0): 
                            index = np.random.randint(0,len(unselectedPathways))
                            mergedList.extend([unselectedPathways[index]])
                        
                        # Add from unassigned list
                        else:     
                            index = np.random.randint(0,len(pathwaySuccessRatiosUnassigned))
                            mergedList.extend([pathwaySuccessRatiosUnassigned[index]])

                    return mergedList 
                
                # We need to pick 1 or more pathways from unassigned list - not enough assigned pathways available
                else:
                    mergedList = pathwaySuccessRatiosSorted

                    indexes = random.sample(range(0, len(pathwaySuccessRatiosUnassigned)), toChooseFromUnassigned)
                    
                    temp = []
                    for index in indexes:
                        temp.append(pathwaySuccessRatiosUnassigned[index])
                    
                    mergedList.extend(temp)
                    return mergedList 

    def __getPathwaysAroundSlicePoint(self, orderedList, slicePoint):
        lowerIndex = -2
        upperIndex = -1
        sliceValue = orderedList[slicePoint][1]

        # Check above slice point
        index = slicePoint
        sameRatio = True

        while (sameRatio == True) and (index >= 0):
            index = index - 1

            if (orderedList[index][1] != sliceValue):
                sameRatio = False
                lowerIndex = index + 1
        
        # Check below slice point
        index = slicePoint
        sameRatio = True

        while (sameRatio == True) and (index < len(orderedList)):
            index = index + 1

            if (orderedList[index][1] != sliceValue):
                sameRatio = False
                upperIndex = index - 1

        if (upperIndex == -1):
            upperIndex = len(orderedList) - 1
        if (lowerIndex == -2):
            lowerIndex = 0
        
        indexChoices = range(lowerIndex, upperIndex + 1)
        indicesToRandomise = (slicePoint - lowerIndex) + 1
        indexes = random.sample(indexChoices, indicesToRandomise)
        
        selectedPathways = orderedList[0:lowerIndex]
        unselectedPathways = orderedList[upperIndex + 1:len(orderedList)]

        for index in indexChoices:
            if index in indexes:
                selectedPathways.extend([orderedList[index]])
            else:
                unselectedPathways.extend([orderedList[index]])
        
        return selectedPathways, unselectedPathways

    def __calcPathwaySuccessRatios(self, topPathways, exerciseProblems, numberPathwayProbs, finalArrayLen):
        ###################### Fitting parameters ######################
        dummySuccess = 0.5 # Success ratio if pathway has never been assigned before. Should be same as for getTopPathwayProblems()
        ################################################################

        normaliseCount = 0
        pathwaySuccessRatios = topPathways

        for exerciseProblem in exerciseProblems:
            pathwaySuccessRatios.extend([[exerciseProblem, dummySuccess]]) 
        
        # print(pathwaySuccessRatios)
        normaliseCount = sum(np.array(pathwaySuccessRatios)[:,1])

        ## Normalise success ratios calculated above
        successRatiosNormalised = []
        successRatiosRounded = []

        for item in pathwaySuccessRatios:
            if (normaliseCount == 0):
                ratio = 1/len(pathwaySuccessRatios)
                successRatiosNormalised += [[item[0], ratio]]
            
            else:    
                ratio = item[1]/normaliseCount
                successRatiosNormalised += [[item[0], ratio]]
        
        ## Ensure probabilties sum to 1 after rounding ratios
        pathwaySuccessDecimalsSorted = sorted(successRatiosNormalised, key=lambda x: (str(int(np.trunc(x[1]*finalArrayLen*10))))[-1], reverse=True)
        
        for item in pathwaySuccessDecimalsSorted:
            successRatiosRounded += [[item[0], np.floor(item[1]*finalArrayLen)/finalArrayLen]]

        error = finalArrayLen - np.sum(np.array(successRatiosRounded)[:, 1])*finalArrayLen
        
        counter = 0
        
        while (error > 0):
            successRatiosRounded[counter][1] += 1/finalArrayLen
            counter += 1
            error = finalArrayLen - np.sum(np.array(successRatiosRounded)[:, 1])*finalArrayLen
        
        return successRatiosRounded

    def GeneratePathways(self):
        ###################### Fitting parameters ######################
        pathwayAssignThreshold = 10
        arrayToPlatypusLen = 100
        poolLength = 8
        ################################################################    

        pathwayrankList = self.__getPathwayRankListByProblem(self.assessProblemId)["pathwayrankList"]
        
        ###################### Initialisation ######################
        pathwaySuccessCount = 0
        problemPool = []
        ############################################################

        for pathway in pathwayrankList:
            globalSuccess = pathway["globalSuccess"]
            pathwaySuccessCount += globalSuccess

        exerciseProblemIds = self.__getExerciseProblemIDs(self.assessProblemId)

        # Convert from array of dictionaries to array of ObjectIds
        for count in range(0, len(exerciseProblemIds)):
            exerciseProblemIds[count] = exerciseProblemIds[count]["_id"]
        
        numExerciseProblems, numPathwayProblems, poolLength = self.__calcNumberExerciseProblems(pathwayAssignCount=pathwaySuccessCount, threshold=pathwayAssignThreshold, exerciseCount=len(exerciseProblemIds), pathwayCount=len(pathwayrankList), poolLen=poolLength)

        exerciseProbsToUse = self.__getRandomExerciseProbs(numExerciseProblems, exerciseProblemIds, [])

        pathwayProbsToUse = self.__getTopPathwayProblems(pathwayrankList, numPathwayProblems)

        pathwaySuccessRatiosNorm  = self.__calcPathwaySuccessRatios(finalArrayLen=arrayToPlatypusLen, topPathways=pathwayProbsToUse, exerciseProblems=exerciseProbsToUse, numberPathwayProbs=numPathwayProblems)
        
        for item in pathwaySuccessRatiosNorm:
            duplicateCount = int(np.floor(item[1]*arrayToPlatypusLen))
            problemDuplicated = [item[0]]*duplicateCount
            problemPool.extend(problemDuplicated)

        return problemPool



def generatePathwayMap(AssessmentProblemId):
    AssessmentProblemId = ObjectId(AssessmentProblemId)
    pathwayMap = mapGenerator(assessmentProblemId=AssessmentProblemId).GeneratePathways()

    return pathwayMap