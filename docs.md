## Get accessKeys

`curl 'https://authentication.arccosgolf.com/accessKeys' \
  -H 'accept: application/json' \
  -H 'content-type: application/json;charset=utf-8' \
  --data-raw '{"email":"<email>","password":"<password>","signedInByFacebook":"F"}'`

> `{
>   "userId":"<user-id>",
>   "accessKey":"<access-key>",
>   "secret":"<some-secret>"
> }`
## Get Token

`curl 'https://authentication.arccosgolf.com/tokens' \
  -H 'accept: application/json' \
  -H 'content-type: application/json;charset=utf-8' \
  --data-raw '{"accessKey":"<access-key>","userId":"<user-id>"}'`

> `{
>   "userId":"<user-id>",
>   "token":"<token>"
> }`

## Get Rounds

`curl 'https://api.arccosgolf.com/v2/users/<user-id>/rounds?limit=<limit>&offSet=<offset>&roundType=flagship' \
  -H 'accept: application/json' \
  -H 'authorization: Bearer: <token>' \
  -H 'content-type: application/json;charset=utf-8'`

> `{
>   "rounds": [
>     {
>       "courseName": "Golfclub Herrnhof",
>       "roundId": <round-id>,
>       "courseId": 36574,
>       "courseVersion": 4,
>       "startTime": "2026-05-21T15:16:24.000Z",
>       "endTime": "2026-05-21T17:33:02.000Z",
>       "lastModifiedTime": "2026-05-21T17:36:38.773Z",
>       "teeId": 3,
>       "noOfHoles": 11,
>       "noOfShots": 64,
>       "par": 44,
>       "overUnder": 20,
>       "noOfAchievements": 0,
>       "isEnded": "T",
>       "isDriverRound": "F",
>       "isDeleted": "F",
>       "shouldIgnore": "F",
>       "isPrivate": "F",
>       "isVerified": "F",
>       "noOfHolesOverride": null,
>       "scoreOverride": null,
>       "roundVersion": 66,
>       "driveHcp": -30,
>       "approachHcp": -30,
>       "chipHcp": -16.9518,
>       "sandHcp": -13.8999,
>       "puttHcp": -25.3338,
>       "includedInLatestHandicap": "T",
>       "notes": null,
>       "roundTypeId": null,
>       "scoreFormatId": null,
>       "ballMakeId": 16,
>       "ballModelId": 59,
>       "roundUUID": "bd7d908c-de3e-4ad6-a0fb-0790a5671402"
>     },
>     ...
>   ],
>   "totalCount": 46
> }`

## Get stats

`curl 'https://api.arccosgolf.com/sga/getDashboardAnalysis/<user-id>?goalHcp=-<target>&roundId=<round-id>' \
  -H 'accept: application/json' \
  -H 'authorization: Bearer: <token>' \
  -H 'content-type: application/json;charset=utf-8'`

> `{
>   "overall": {
>     "overallSection": {
>       "sga": -6.5,
>       "drivingSga": -2.7,
>       "approachSga": -5.2,
>       "shortSga": 1.2,
>       "puttingSga": 0.3
>     },
>     "paceOfPlay": "02:16:38",
>     "noOfHoles": 11,
>     "holeScores": [
>       {
>         "holeId": 1,
>         "netScore": 2,
>         "noOfShots": 6,
>         "par": 4
>       },
>       {
>         "holeId": 2,
>         "netScore": 1,
>         "noOfShots": 4,
>         "par": 3
>       },
>       {
>         "holeId": 3,
>         "netScore": 4,
>         "noOfShots": 9,
>         "par": 5
>       },
>       {
>         "holeId": 4,
>         "netScore": 1,
>         "noOfShots": 5,
>         "par": 4
>       },
>       {
>         "holeId": 5,
>         "netScore": 3,
>         "noOfShots": 8,
>         "par": 5
>       },
>       {
>         "holeId": 6,
>         "netScore": 4,
>         "noOfShots": 8,
>         "par": 4
>       },
>       {
>         "holeId": 7,
>         "netScore": 2,
>         "noOfShots": 5,
>         "par": 3
>       },
>       {
>         "holeId": 8,
>         "netScore": 1,
>         "noOfShots": 6,
>         "par": 5
>       },
>       {
>         "holeId": 9,
>         "netScore": 0,
>         "noOfShots": 4,
>         "par": 4
>       },
>       {
>         "holeId": 10,
>         "netScore": 1,
>         "noOfShots": 5,
>         "par": 4
>       },
>       {
>         "holeId": 11,
>         "netScore": 1,
>         "noOfShots": 4,
>         "par": 3
>       }
>     ],
>     "caddieInsights": {
>       "helping": [
>         {
>           "shotType": "short",
>           "label": "chipByPinDistance",
>           "sga": 1.4,
>           "fromDistance": {
>             "unit": "Yards",
>             "value": "0-25"
>           },
>           "slabId": 9,
>           "insightId": 11
>         },
>         {
>           "shotType": "putting",
>           "label": "puttingByLength",
>           "sga": 0.7,
>           "fromDistance": {
>             "unit": "ft",
>             "value": "50+"
>           },
>           "slabId": 14,
>           "insightId": 18
>         },
>         {
>           "shotType": "putting",
>           "label": "puttingByLength",
>           "sga": 0.4,
>           "fromDistance": {
>             "unit": "ft",
>             "value": "0-10"
>           },
>           "slabId": 11,
>           "insightId": 15
>         }
>       ],
>       "hurting": [
>         {
>           "shotType": "approach",
>           "label": "approachByTerrain",
>           "sga": -3.6,
>           "from": "fairway",
>           "insightId": 8
>         },
>         {
>           "shotType": "approach",
>           "label": "approachByTerrain",
>           "sga": -2,
>           "from": "tee",
>           "insightId": 7
>         },
>         {
>           "shotType": "approach",
>           "label": "approachByPinDistance",
>           "sga": -1.9,
>           "fromDistance": {
>             "unit": "Yards",
>             "value": "150-200"
>           },
>           "slabId": 7,
>           "insightId": 5
>         }
>       ]
>     },
>     "scoreAnalysis": {
>       "parsData": {
>         "par3": {
>           "score": 4.3,
>           "sga": 0
>         },
>         "par4": {
>           "score": 5.6,
>           "sga": -0.3
>         },
>         "par5": {
>           "score": 7.7,
>           "sga": -1.7
>         }
>       },
>       "birdies": {
>         "actual": {
>           "unit": "percent",
>           "value": 0
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 2
>         }
>       },
>       "bogies": {
>         "actual": {
>           "unit": "percent",
>           "value": 45
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 50
>         }
>       },
>       "doubleplus": {
>         "actual": {
>           "unit": "percent",
>           "value": 45
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 36
>         }
>       },
>       "pars": {
>         "actual": {
>           "unit": "percent",
>           "value": 9
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 19
>         }
>       },
>       "birdiesRaw": {
>         "actual": 0,
>         "goal": 0
>       },
>       "bogiesRaw": {
>         "actual": 5,
>         "goal": 6
>       },
>       "doubleplusRaw": {
>         "actual": 5,
>         "goal": 4
>       },
>       "parsRaw": {
>         "actual": 1,
>         "goal": 2
>       }
>     },
>     "traditionalStats": {
>       "averageDriveDistance": {
>         "unit": "Yards",
>         "value": 141
>       },
>       "longestDrive": {
>         "unit": "Yards",
>         "value": 176
>       },
>       "averageApproachDistance": {
>         "unit": "Yards",
>         "value": 92
>       },
>       "totalPutts": {
>         "value": 23,
>         "zeroPutt": 0,
>         "onePutt": 1,
>         "twoPutt": 8,
>         "threePutt": 2
>       },
>       "gir": {
>         "noOfGirsHit": 0,
>         "noOfHoles": 11
>       },
>       "hitFairway": {
>         "fairways": 3,
>         "totalFairways": 8
>       },
>       "upAndDown": {
>         "upAndDownSuccess": 1,
>         "totalChances": 7
>       },
>       "totalDistance": {
>         "unit": "Yards",
>         "value": 3377
>       }
>     }
>   },
>   "driving": {
>     "sga": -2.7,
>     "historicSga": -3.7,
>     "historicRoundThreshold": 5,
>     "historicRoundCount": 5,
>     "handicap": -30,
>     "distanceVsAccuracy": {
>       "sgDistance": -0.9,
>       "sgAccuracy": -1.9,
>       "sgPenalties": 0
>     },
>     "drivingDistance": {
>       "averageDistance": {
>         "unit": "Yards",
>         "value": 141
>       },
>       "goal": {
>         "unit": "Yards",
>         "value": 158
>       },
>       "drivingCount": 8,
>       "longestDrive": {
>         "unit": "Yards",
>         "value": 176
>       }
>     },
>     "drivingAccuracy": {
>       "hitFairway": {
>         "percentage": {
>           "unit": "percent",
>           "value": 38
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 41
>         },
>         "shotsCount": 3,
>         "sga": -0.2
>       },
>       "missedLeft": {
>         "percentage": {
>           "unit": "percent",
>           "value": 25
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 27
>         },
>         "shotsCount": 2,
>         "sga": -0.6
>       },
>       "missedRight": {
>         "percentage": {
>           "unit": "percent",
>           "value": 38
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 31
>         },
>         "shotsCount": 3,
>         "sga": -2
>       }
>     },
>     "drivingByHoleLength": [
>       {
>         "slabId": 1,
>         "slab": {
>           "unit": "Yards",
>           "value": "0-350"
>         },
>         "sga": 0.3,
>         "shotsCount": 4
>       },
>       {
>         "slabId": 2,
>         "slab": {
>           "unit": "Yards",
>           "value": "350-400"
>         },
>         "sga": -1,
>         "shotsCount": 1
>       },
>       {
>         "slabId": 3,
>         "slab": {
>           "unit": "Yards",
>           "value": "400-450"
>         },
>         "sga": -0.8,
>         "shotsCount": 1
>       },
>       {
>         "slabId": 4,
>         "slab": {
>           "unit": "Yards",
>           "value": "450+"
>         },
>         "sga": -1.2,
>         "shotsCount": 2
>       }
>     ],
>     "drivingByHoleShape": [
>       {
>         "holeShapeId": 1,
>         "holeShape": "dogleg left",
>         "shotsCount": 3,
>         "sga": -0.2
>       },
>       {
>         "holeShapeId": 2,
>         "holeShape": "straight",
>         "shotsCount": 3,
>         "sga": -2.6
>       },
>       {
>         "holeShapeId": 3,
>         "holeShape": "dogleg right",
>         "shotsCount": 2,
>         "sga": 0.1
>       }
>     ]
>   },
>   "approach": {
>     "sga": -5.2,
>     "historicSga": -11.9,
>     "handicap": -30,
>     "approachByPinDistance": [
>       {
>         "slabId": 5,
>         "slab": {
>           "unit": "Yards",
>           "value": "50-100"
>         },
>         "sga": -0.4,
>         "shotsCount": 9
>       },
>       {
>         "slabId": 6,
>         "slab": {
>           "unit": "Yards",
>           "value": "100-150"
>         },
>         "sga": -1.7,
>         "shotsCount": 4
>       },
>       {
>         "slabId": 7,
>         "slab": {
>           "unit": "Yards",
>           "value": "150-200"
>         },
>         "sga": -1.9,
>         "shotsCount": 5
>       },
>       {
>         "slabId": 8,
>         "slab": {
>           "unit": "Yards",
>           "value": "200+"
>         },
>         "sga": -1.2,
>         "shotsCount": 4
>       }
>     ],
>     "approachByTerrain": [
>       {
>         "terrainId": 5,
>         "terrain": "tee",
>         "shotsCount": 3,
>         "sga": -2
>       },
>       {
>         "terrainId": 6,
>         "terrain": "fairway",
>         "shotsCount": 13,
>         "sga": -3.6
>       },
>       {
>         "terrainId": 7,
>         "terrain": "rough",
>         "shotsCount": 6,
>         "sga": 0.3
>       },
>       {
>         "terrainId": 8,
>         "terrain": "sand",
>         "shotsCount": 0,
>         "sga": null
>       }
>     ],
>     "gir": {
>       "gir": {
>         "unit": "percent",
>         "value": 0
>       },
>       "goal": {
>         "unit": "percent",
>         "value": 20
>       },
>       "left": {
>         "unit": "percent",
>         "value": 9
>       },
>       "right": {
>         "unit": "percent",
>         "value": 0
>       },
>       "short": {
>         "unit": "percent",
>         "value": 91
>       },
>       "long": {
>         "unit": "percent",
>         "value": 0
>       },
>       "girApproach": {
>         "actual": {
>           "unit": "ft",
>           "value": 0
>         },
>         "goal": {
>           "unit": "ft",
>           "value": 36
>         }
>       },
>       "allApproach": {
>         "actual": {
>           "unit": "ft",
>           "value": 149
>         },
>         "goal": {
>           "unit": "ft",
>           "value": 85
>         }
>       },
>       "girRaw": 0,
>       "leftRaw": 1,
>       "rightRaw": 0,
>       "shortRaw": 10,
>       "longRaw": 0
>     },
>     "approachDistance": {
>       "unit": "Yards",
>       "value": 92
>     },
>     "traditionalGir": {
>       "noOfGirsHit": 0,
>       "noOfHoles": 11
>     },
>     "historicRoundThreshold": 5,
>     "historicRoundCount": 5
>   },
>   "short": {
>     "sga": 1.2,
>     "historicSga": 1.4,
>     "historicRoundThreshold": 5,
>     "historicRoundCount": 5,
>     "handicap": -5,
>     "chipByPinDistance": [
>       {
>         "slabId": 9,
>         "slab": {
>           "unit": "Yards",
>           "value": "0-25"
>         },
>         "sga": 1.4,
>         "shotsCount": 5
>       },
>       {
>         "slabId": 10,
>         "slab": {
>           "unit": "Yards",
>           "value": "25-50"
>         },
>         "sga": 0,
>         "shotsCount": 1
>       }
>     ],
>     "chippingAccuracy": [
>       {
>         "slabId": 9,
>         "slab": {
>           "unit": "Yards",
>           "value": "0-25"
>         },
>         "avgDistanceToPin": {
>           "unit": "ft",
>           "value": 15
>         },
>         "avgDistanceToPinGoal": {
>           "unit": "ft",
>           "value": 20
>         },
>         "missedGreens": {
>           "unit": "percent",
>           "value": 0
>         },
>         "missedGreensGoal": {
>           "unit": "percent",
>           "value": 12
>         },
>         "upAndDown": {
>           "unit": "percent",
>           "value": 20
>         },
>         "upAndDownGoal": {
>           "unit": "percent",
>           "value": 23
>         }
>       },
>       {
>         "slabId": 10,
>         "slab": {
>           "unit": "Yards",
>           "value": "25-50"
>         },
>         "avgDistanceToPin": {
>           "unit": "ft",
>           "value": 75
>         },
>         "avgDistanceToPinGoal": {
>           "unit": "ft",
>           "value": 30
>         },
>         "missedGreens": {
>           "unit": "percent",
>           "value": 0
>         },
>         "missedGreensGoal": {
>           "unit": "percent",
>           "value": 27
>         },
>         "upAndDown": {
>           "unit": "percent",
>           "value": 0
>         },
>         "upAndDownGoal": {
>           "unit": "percent",
>           "value": 11
>         }
>       }
>     ],
>     "sandByPinDistance": [
>       {
>         "slabId": 9,
>         "slab": {
>           "unit": "Yards",
>           "value": "0-25"
>         },
>         "sga": -0.2,
>         "shotsCount": 2
>       },
>       {
>         "slabId": 10,
>         "slab": {
>           "unit": "Yards",
>           "value": "25-50"
>         },
>         "sga": null,
>         "shotsCount": 0
>       }
>     ],
>     "sandAccuracy": [
>       {
>         "slabId": 9,
>         "slab": {
>           "unit": "Yards",
>           "value": "0-25"
>         },
>         "avgDistanceToPin": {
>           "unit": "ft",
>           "value": 19
>         },
>         "avgDistanceToPinGoal": {
>           "unit": "ft",
>           "value": 29
>         },
>         "missedGreens": {
>           "unit": "percent",
>           "value": 50
>         },
>         "missedGreensGoal": {
>           "unit": "percent",
>           "value": 31
>         },
>         "upAndDown": {
>           "unit": "percent",
>           "value": 0
>         },
>         "upAndDownGoal": {
>           "unit": "percent",
>           "value": 13
>         }
>       },
>       {
>         "slabId": 10,
>         "slab": {
>           "unit": "Yards",
>           "value": "25-50"
>         },
>         "avgDistanceToPin": {
>           "unit": "ft",
>           "value": 0
>         },
>         "avgDistanceToPinGoal": {
>           "unit": "ft",
>           "value": 37
>         },
>         "missedGreens": {
>           "unit": "percent",
>           "value": 0
>         },
>         "missedGreensGoal": {
>           "unit": "percent",
>           "value": 38
>         },
>         "upAndDown": {
>           "unit": "percent",
>           "value": 0
>         },
>         "upAndDownGoal": {
>           "unit": "percent",
>           "value": 8
>         }
>       }
>     ]
>   },
>   "putting": {
>     "sga": 0.3,
>     "historicSga": -3.9,
>     "historicRoundThreshold": 5,
>     "historicRoundCount": 5,
>     "handicap": -18,
>     "puttingByHole": {
>       "holeSga": [
>         {
>           "holeId": 2,
>           "sga": 0.8
>         },
>         {
>           "holeId": 11,
>           "sga": 0.2
>         },
>         {
>           "holeId": 4,
>           "sga": 0.1
>         },
>         {
>           "holeId": 7,
>           "sga": 0.2
>         },
>         {
>           "holeId": 9,
>           "sga": 0.7
>         },
>         {
>           "holeId": 10,
>           "sga": -0.3
>         },
>         {
>           "holeId": 1,
>           "sga": 0.1
>         },
>         {
>           "holeId": 8,
>           "sga": 0.1
>         },
>         {
>           "holeId": 6,
>           "sga": -0.7
>         },
>         {
>           "holeId": 3,
>           "sga": -0.7
>         },
>         {
>           "holeId": 5,
>           "sga": -0.3
>         }
>       ],
>       "puttValue": 36
>     },
>     "puttingByLength": [
>       {
>         "slabId": 11,
>         "slab": {
>           "unit": "ft",
>           "value": "0-10"
>         },
>         "sga": 0.4,
>         "shotsCount": 15
>       },
>       {
>         "slabId": 12,
>         "slab": {
>           "unit": "ft",
>           "value": "10-25"
>         },
>         "sga": 0.2,
>         "shotsCount": 5
>       },
>       {
>         "slabId": 13,
>         "slab": {
>           "unit": "ft",
>           "value": "25-50"
>         },
>         "sga": -1,
>         "shotsCount": 2
>       },
>       {
>         "slabId": 14,
>         "slab": {
>           "unit": "ft",
>           "value": "50+"
>         },
>         "sga": 0.7,
>         "shotsCount": 1
>       }
>     ],
>     "avgPuttsPerRound": {
>       "onePutt": {
>         "actual": {
>           "unit": "percent",
>           "value": 9
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 16
>         }
>       },
>       "twoPutt": {
>         "actual": {
>           "unit": "percent",
>           "value": 73
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 61
>         }
>       },
>       "threePutt": {
>         "actual": {
>           "unit": "percent",
>           "value": 18
>         },
>         "goal": {
>           "unit": "percent",
>           "value": 22
>         }
>       },
>       "perHole": {
>         "actual": 2.1,
>         "goal": 2
>       },
>       "perRound": {
>         "actual": 23,
>         "goal": 36.2
>       },
>       "perGir": {
>         "actual": null,
>         "goal": 2.4
>       },
>       "zeroPuttRaw": {
>         "actual": 0,
>         "goal": 0
>       },
>       "onePuttRaw": {
>         "actual": 1,
>         "goal": 2
>       },
>       "twoPuttRaw": {
>         "actual": 8,
>         "goal": 7
>       },
>       "threePuttRaw": {
>         "actual": 2,
>         "goal": 2
>       }
>     }
>   }
> }`

## GET round

`curl 'https://api.arccosgolf.com/sga/getDashboardAnalysis/<user-id>?goalHcp=-<target>&roundId=<round-id>' \
  -H 'accept: application/json' \
  -H 'authorization: Bearer: <token>' \
  -H 'content-type: application/json;charset=utf-8'`

> `{
    "roundId": 28559857,
    "roundVersion": 92,
    "courseId": 36574,
    "courseVersion": 4,
    "userId": "b885a72037e511efac017725d7ba33d1",
    "startTime": "2026-07-12T12:44:21.000000Z",
    "endTime": "2026-07-12T16:57:40.000000Z",
    "lastModifiedTime": "2026-07-12T16:58:55.855000Z",
    "noOfHoles": 18,
    "noOfShots": 99,
    "shouldIgnore": "F",
    "teeId": 3,
    "isPrivate": "F",
    "isVerified": "F",
    "isEnded": "T",
    "isDriverRound": "F",
    "noOfHolesOverride": null,
    "scoreOverride": null,
    "courseName": "Golfclub Herrnhof",
    "overUnder": 27,
    "roundTypeId": null,
    "scoreFormatId": null,
    "roundUUID": "820bb187-8453-4a2a-b9b1-d7dbd4bcfb75",
    "holes": [
        {
            "holeId": 1,
            "noOfShots": 5,
            "isGir": "T",
            "putts": 3,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T12:46:43.000000Z",
            "endTime": "2026-07-12T12:55:00.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.301303218683,
            "pinLong": 11.389702435445,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.3009963,
                    "startLong": 11.3929979,
                    "endLat": 49.3004123,
                    "endLong": 11.3907044,
                    "distance": 179.006,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:46:43.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "9d7c3927-ed3b-461d-bfc4-44530c318b3d",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.3004123,
                    "startLong": 11.3907044,
                    "endLat": 49.3012529,
                    "endLong": 11.38973,
                    "distance": 117.313,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:50:46.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "ae052527-6c18-4025-aef3-2b1b290f7e30",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.3012529,
                    "startLong": 11.38973,
                    "endLat": 49.301285148965,
                    "endLong": 11.389712334036,
                    "distance": 3.80978,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:54:40.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "18666f4c-ad14-4b0a-8bcb-ddbea5f6f4e0",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.301285148965,
                    "startLong": 11.389712334036,
                    "endLat": 49.301298055907,
                    "endLong": 11.389705263615,
                    "distance": 1.52478,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:54:59.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7bf87763-0a05-4056-b851-92ac18fad142",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 1,
                    "startLat": 49.301298055907,
                    "startLong": 11.389705263615,
                    "endLat": 49.301303218683,
                    "endLong": 11.389702435445,
                    "distance": 0.609912,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:55:00.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7e7c865f-a1da-4c12-bdea-caa2012196fa",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 2,
            "noOfShots": 3,
            "isGir": "F",
            "putts": 1,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T12:57:55.000000Z",
            "endTime": "2026-07-12T13:02:18.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.300346727926,
            "pinLong": 11.390052496957,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.3011051,
                    "startLong": 11.3885384,
                    "endLat": 49.3003508,
                    "endLong": 11.3897516,
                    "distance": 121.75,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T12:57:55.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "a2fcfa9f-f676-48e7-8335-69bc79a099a2",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.3003508,
                    "startLong": 11.3897516,
                    "endLat": 49.300341095094,
                    "endLong": 11.390056908131,
                    "distance": 22.2315,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:00:55.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "5809e04e-2d64-4b2f-a036-0ef9bcc7b6a9",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.300341095094,
                    "startLong": 11.390056908131,
                    "endLat": 49.300346727926,
                    "endLong": 11.390052496957,
                    "distance": 0.703833,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:02:18.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "cab52e53-ae73-4fb5-8724-f819a2d03e35",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 3,
            "noOfShots": 6,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T13:07:50.000000Z",
            "endTime": "2026-07-12T13:21:58.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 4,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.3011564,
            "pinLong": 11.3829056,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.3000272,
                    "startLong": 11.3888128,
                    "endLat": 49.300208,
                    "endLong": 11.38662,
                    "distance": 160.747,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:07:50.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "0a0cc378-ace3-4e96-b079-b0a220e3d079",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 3,
                    "clubId": 23,
                    "startLat": 49.300208,
                    "startLong": 11.38662,
                    "endLat": 49.3005168,
                    "endLong": 11.384424,
                    "distance": 163.367,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:12:16.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "22725b8e-16d9-4f4b-8771-2f7c8d730c46",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.3005168,
                    "startLong": 11.384424,
                    "endLat": 49.3011148,
                    "endLong": 11.3834796,
                    "distance": 95.6085,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:16:51.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "145d43fc-fe93-4274-9ed2-1ae97c1d424a",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.3011148,
                    "startLong": 11.3834796,
                    "endLat": 49.301233,
                    "endLong": 11.3829841,
                    "distance": 38.3603,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:19:24.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "36901553-4792-4349-98f4-84c0a70040b0",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.301233,
                    "startLong": 11.3829841,
                    "endLat": 49.301160961707,
                    "endLong": 11.382910274849,
                    "distance": 9.64457,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:21:40.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "e86b78ad-46d9-4e5c-a169-627f25fcddc0",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.301160961707,
                    "startLong": 11.382910274849,
                    "endLat": 49.3011564,
                    "endLong": 11.3829056,
                    "distance": 0.610726,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:21:58.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7d3c75b6-d683-48db-b5e8-2f5ca03fc745",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 4,
            "noOfShots": 5,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T13:25:28.000000Z",
            "endTime": "2026-07-12T13:34:49.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.2995835,
            "pinLong": 11.3865432,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.3007918,
                    "startLong": 11.3829372,
                    "endLat": 49.2998237,
                    "endLong": 11.3848648,
                    "distance": 176.769,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:25:28.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "dcb7e7da-0ff7-451d-8508-ec18f224ebdd",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2998237,
                    "startLong": 11.3848648,
                    "endLat": 49.2997895,
                    "endLong": 11.3867459,
                    "distance": 136.868,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:30:12.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "d8554302-a5ae-4c22-b5b6-aff9590c96a4",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2997895,
                    "startLong": 11.3867459,
                    "endLat": 49.2995735,
                    "endLong": 11.38656,
                    "distance": 27.5662,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:33:30.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "d4556ef7-357c-4931-9faf-ce4f2212e6f9",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2995735,
                    "startLong": 11.38656,
                    "endLat": 49.299579804017,
                    "endLong": 11.386549409252,
                    "distance": 1.04158,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:34:48.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f51c4d4a-bba6-43fa-940c-28ad005b8753",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.299579804017,
                    "startLong": 11.386549409252,
                    "endLat": 49.2995835,
                    "endLong": 11.3865432,
                    "distance": 0.610668,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:34:49.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f118ffe5-b2a9-43b2-b585-960fe27dec81",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 5,
            "noOfShots": 6,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T13:39:33.000000Z",
            "endTime": "2026-07-12T13:52:14.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "T",
            "isFairWayLeft": "F",
            "approachShotId": 4,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.300036130302,
            "pinLong": 11.390866480525,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2989603,
                    "startLong": 11.3857949,
                    "endLat": 49.2992844,
                    "endLong": 11.3881392,
                    "distance": 174.275,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:39:33.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "4763913e-24ab-4a96-8c99-a85b5ed84fed",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 3,
                    "clubId": 23,
                    "startLat": 49.2992844,
                    "startLong": 11.3881392,
                    "endLat": 49.2994481,
                    "endLong": 11.3891668,
                    "distance": 76.9251,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:43:49.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "ddde59c4-1a68-41f7-ab53-51ad84b3dfa9",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2994481,
                    "startLong": 11.3891668,
                    "endLat": 49.3000783,
                    "endLong": 11.3905749,
                    "distance": 124.1,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:46:37.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "e6260aeb-9aac-46d0-a4d3-215c6b6571f0",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.3000783,
                    "startLong": 11.3905749,
                    "endLat": 49.3000145,
                    "endLong": 11.3908769,
                    "distance": 23.0825,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:50:23.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "e31aad9a-27d0-4ef9-8fed-8a41e2021edb",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.3000145,
                    "startLong": 11.3908769,
                    "endLat": 49.3000309,
                    "endLong": 11.390869,
                    "distance": 1.9123,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:52:04.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "b87ed152-c2de-4305-8056-8cc684c2487e",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.3000309,
                    "startLong": 11.390869,
                    "endLat": 49.300036130302,
                    "endLong": 11.390866480525,
                    "distance": 0.609871,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:52:14.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "3f575896-45e1-44a0-9a6a-63947e5c9fb8",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 6,
            "noOfShots": 6,
            "isGir": "F",
            "putts": 3,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T13:56:14.000000Z",
            "endTime": "2026-07-12T14:05:21.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.29881,
            "pinLong": 11.3883075,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2998282,
                    "startLong": 11.3923128,
                    "endLat": 49.2988991,
                    "endLong": 11.3905105,
                    "distance": 166.915,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:56:14.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "d445f0c3-fe28-445f-8913-ab9f36f32e78",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2988991,
                    "startLong": 11.3905105,
                    "endLat": 49.2989228,
                    "endLong": 11.3889265,
                    "distance": 115.239,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T13:59:44.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "c7efefbf-6145-4c7b-ba7d-75d6fbe0b159",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2989228,
                    "startLong": 11.3889265,
                    "endLat": 49.2987957,
                    "endLong": 11.3884193,
                    "distance": 39.5057,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:02:54.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "1419f2e5-5bda-49c2-9b15-0bda06e03526",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2987957,
                    "startLong": 11.3884193,
                    "endLat": 49.298806306818,
                    "endLong": 11.388336374057,
                    "distance": 6.14574,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:04:42.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "a511913c-daf3-4b63-bf58-e89b1195a162",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.298806306818,
                    "startLong": 11.388336374057,
                    "endLat": 49.298808944806,
                    "endLong": 11.388315749731,
                    "distance": 1.52849,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:05:12.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "968eb198-3425-4366-804c-af6dc53c841e",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.298808944806,
                    "startLong": 11.388315749731,
                    "endLat": 49.29881,
                    "endLong": 11.3883075,
                    "distance": 0.611397,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:05:21.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "dea85904-1d6b-483b-b392-050e2c57ee15",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 7,
            "noOfShots": 4,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T14:08:56.000000Z",
            "endTime": "2026-07-12T14:14:57.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.297933243471,
            "pinLong": 11.385424320134,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2982295,
                    "startLong": 11.3877101,
                    "endLat": 49.2981752,
                    "endLong": 11.3855232,
                    "distance": 159.177,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:08:56.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "ca9ef367-f0f8-4cad-b727-b63a587f91ae",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2981752,
                    "startLong": 11.3855232,
                    "endLat": 49.2979216,
                    "endLong": 11.3853675,
                    "distance": 30.3929,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:13:12.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "cedcf86a-185e-4eff-a60b-75b1a65ca73d",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2979216,
                    "startLong": 11.3853675,
                    "endLat": 49.297931600003,
                    "endLong": 11.385416299999,
                    "distance": 3.7196,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:14:56.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "58ceae31-afb7-4f5c-8a79-4af2848e370f",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 1,
                    "startLat": 49.297931600003,
                    "startLong": 11.385416299999,
                    "endLat": 49.297933243471,
                    "endLong": 11.385424320134,
                    "distance": 0.611304,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:14:57.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "83fea5f7-b97b-44df-84fb-cea37143f891",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 8,
            "noOfShots": 7,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T14:22:13.000000Z",
            "endTime": "2026-07-12T14:35:40.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 5,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.29711901773,
            "pinLong": 11.39121639127,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2971233,
                    "startLong": 11.3855368,
                    "endLat": 49.2970048,
                    "endLong": 11.3879783,
                    "distance": 178.072,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:22:13.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "8eb9ce21-a30b-45ad-8ca9-266974ad5883",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 3,
                    "clubId": 23,
                    "startLat": 49.2970048,
                    "startLong": 11.3879783,
                    "endLat": 49.2965361,
                    "endLong": 11.3895533,
                    "distance": 125.861,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:26:32.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "cb8d6109-c532-4397-aedc-c1805ee32f8b",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 9,
                    "clubId": 16,
                    "startLat": 49.2965361,
                    "startLong": 11.3895533,
                    "endLat": 49.2966812,
                    "endLong": 11.3908663,
                    "distance": 96.8566,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:29:40.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "c5a2a987-5c88-4b88-b2a5-65c224034b12",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2966812,
                    "startLong": 11.3908663,
                    "endLat": 49.2971171,
                    "endLong": 11.391542,
                    "distance": 69.034,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:31:53.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f832260f-de23-476c-9c2c-92ff26a983db",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2971171,
                    "startLong": 11.391542,
                    "endLat": 49.2971873,
                    "endLong": 11.3912165,
                    "distance": 24.9295,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:33:47.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "bdd53b44-ca7a-443c-b283-5f2145e75971",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2971873,
                    "startLong": 11.3912165,
                    "endLat": 49.2971245,
                    "endLong": 11.3912164,
                    "distance": 6.98434,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:35:26.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "565a6f44-132f-4e5d-8259-43eaf9054aa9",
                    "tourQuality": null
                },
                {
                    "shotId": 7,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2971245,
                    "startLong": 11.3912164,
                    "endLat": 49.29711901773,
                    "endLong": 11.39121639127,
                    "distance": 0.609714,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:35:40.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "40c2f16a-4999-4ba3-ae9f-2219d55eefb0",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 9,
            "noOfShots": 5,
            "isGir": "T",
            "putts": 3,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T14:40:43.000000Z",
            "endTime": "2026-07-12T14:47:52.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "T",
            "isFairWayLeft": "F",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.2993165,
            "pinLong": 11.3942646,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2974976,
                    "startLong": 11.3928811,
                    "endLat": 49.2988007,
                    "endLong": 11.3938425,
                    "distance": 160.913,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:40:43.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "993cb1d4-8ae4-4989-b146-8d510fee2d7a",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2988007,
                    "startLong": 11.3938425,
                    "endLat": 49.299248,
                    "endLong": 11.394097,
                    "distance": 53.0789,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:44:45.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "eca178bf-9233-4036-818a-9a532571d9b2",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.299248,
                    "startLong": 11.394097,
                    "endLat": 49.29930630992,
                    "endLong": 11.394239667708,
                    "distance": 12.2363,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:47:12.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "500fe150-7504-4e52-b4d4-72f6586a7718",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.29930630992,
                    "startLong": 11.394239667708,
                    "endLat": 49.299313588549,
                    "endLong": 11.394257476487,
                    "distance": 1.52742,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:47:51.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "6cb35b85-28ee-4959-8cb2-87d724bc3ce2",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.299313588549,
                    "startLong": 11.394257476487,
                    "endLat": 49.2993165,
                    "endLong": 11.3942646,
                    "distance": 0.610969,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:47:52.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7c90790c-c82f-47a8-b490-674f5e511e77",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 10,
            "noOfShots": 5,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T14:51:09.000000Z",
            "endTime": "2026-07-12T14:57:56.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.297083159222,
            "pinLong": 11.393578983843,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2988349,
                    "startLong": 11.3949584,
                    "endLat": 49.2977401,
                    "endLong": 11.3942844,
                    "distance": 131.257,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:51:09.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "451aa417-222c-4369-992c-a7162bc23630",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2977401,
                    "startLong": 11.3942844,
                    "endLat": 49.297672814062,
                    "endLong": 11.393914439062,
                    "distance": 27.9301,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:54:52.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "8ff4a094-43a0-49de-af4c-af603afa37e4",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.297672814062,
                    "startLong": 11.393914439062,
                    "endLat": 49.297216352152,
                    "endLong": 11.393484857074,
                    "distance": 59.6108,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:56:30.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "0a91bf24-7488-4b4a-9e26-b9fae8b1f629",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.297216352152,
                    "startLong": 11.393484857074,
                    "endLat": 49.297088067359,
                    "endLong": 11.393575515298,
                    "distance": 15.7174,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:57:55.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "30cf8888-c31d-4d22-81c6-9c15ac5bcb6b",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.297088067359,
                    "startLong": 11.393575515298,
                    "endLat": 49.297083159222,
                    "endLong": 11.393578983843,
                    "distance": 0.601342,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T14:57:56.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "6df96a9a-67cd-4b74-9f31-4c12cd8176bf",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 11,
            "noOfShots": 4,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T15:03:33.000000Z",
            "endTime": "2026-07-12T15:09:50.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.2963704,
            "pinLong": 11.3917709,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2960618,
                    "startLong": 11.3942339,
                    "endLat": 49.2966948,
                    "endLong": 11.3922874,
                    "distance": 158.119,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:03:33.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "b815f55b-81ab-4a06-a83f-4619e4fe57e3",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2966948,
                    "startLong": 11.3922874,
                    "endLat": 49.29637,
                    "endLong": 11.3918281,
                    "distance": 49.203,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:07:57.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "c0569e2d-df1b-44c8-b9c7-41cfb7fcc8b7",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.29637,
                    "startLong": 11.3918281,
                    "endLat": 49.296370341218,
                    "endLong": 11.391779306023,
                    "distance": 3.54931,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:09:49.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "df367145-c6ab-4bca-9090-b4b29245588e",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.296370341218,
                    "startLong": 11.391779306023,
                    "endLat": 49.2963704,
                    "endLong": 11.3917709,
                    "distance": 0.611461,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:09:50.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "acdf38b4-603d-445a-aa64-3e8d7adb59ce",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 12,
            "noOfShots": 8,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T15:18:49.000000Z",
            "endTime": "2026-07-12T15:32:31.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 6,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.296753156535,
            "pinLong": 11.38447012986,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2959498,
                    "startLong": 11.3894643,
                    "endLat": 49.296271,
                    "endLong": 11.3878248,
                    "distance": 124.488,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:18:49.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "bd53c57e-77ff-48c8-8694-e21d966b8899",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 3,
                    "clubId": 23,
                    "startLat": 49.296271,
                    "startLong": 11.3878248,
                    "endLat": 49.2963122,
                    "endLong": 11.3868928,
                    "distance": 67.9454,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:22:31.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "8016de8f-a5a6-4cc0-a004-e7b019b7ad0b",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 38,
                    "clubId": 24,
                    "startLat": 49.2963122,
                    "startLong": 11.3868928,
                    "endLat": 49.2964289,
                    "endLong": 11.3862848,
                    "distance": 46.0891,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:24:49.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7e9e1abb-3e4f-41f2-a6c8-95b69d36ede1",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2964289,
                    "startLong": 11.3862848,
                    "endLat": 49.2968128,
                    "endLong": 11.385246,
                    "distance": 86.7871,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:27:07.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "abe872fa-8ced-48e1-942b-ecbd83a75f14",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2968128,
                    "startLong": 11.385246,
                    "endLat": 49.2968276,
                    "endLong": 11.3847351,
                    "distance": 37.1973,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:29:23.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "5352cc1a-e279-4f30-8b4f-4858792a380d",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2968276,
                    "startLong": 11.3847351,
                    "endLat": 49.2967745,
                    "endLong": 11.3845677,
                    "distance": 13.5326,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:31:06.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "73c0a1fe-e7c9-431f-b17b-5f0d30d8761a",
                    "tourQuality": null
                },
                {
                    "shotId": 7,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2967745,
                    "startLong": 11.3845677,
                    "endLat": 49.2967549,
                    "endLong": 11.3844781,
                    "distance": 6.87204,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:32:09.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "3d22f73d-ffc9-478c-982f-977cfe578df2",
                    "tourQuality": null
                },
                {
                    "shotId": 8,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2967549,
                    "startLong": 11.3844781,
                    "endLat": 49.296753156535,
                    "endLong": 11.38447012986,
                    "distance": 0.611285,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:32:31.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "281ca584-7097-4ccc-b860-bdad2387a4ad",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 13,
            "noOfShots": 5,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T15:37:40.000000Z",
            "endTime": "2026-07-12T15:47:52.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.295447441601,
            "pinLong": 11.381862424314,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2960787,
                    "startLong": 11.3860985,
                    "endLat": 49.2959684,
                    "endLong": 11.3839384,
                    "distance": 157.598,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:37:40.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "5b531d46-e80e-4581-b771-c4c3ec63ea6f",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2959684,
                    "startLong": 11.3839384,
                    "endLat": 49.295451321622,
                    "endLong": 11.382560298649,
                    "distance": 115.564,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:41:59.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "b5f508d6-5f96-407c-9242-c3ae71501b27",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.295451321622,
                    "startLong": 11.382560298649,
                    "endLat": 49.2955285,
                    "endLong": 11.3820363,
                    "distance": 39.0691,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:45:56.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "5444b1c4-e19a-403c-80a7-ac1c8890292b",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2955285,
                    "startLong": 11.3820363,
                    "endLat": 49.295450629737,
                    "endLong": 11.381869263057,
                    "distance": 14.9206,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:47:51.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f8cddd23-e97d-4963-8f82-c7302f6b02bd",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.295450629737,
                    "startLong": 11.381869263057,
                    "endLat": 49.295447441601,
                    "endLong": 11.381862424314,
                    "distance": 0.610871,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:47:52.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f5b74181-cdfc-4e5e-870c-ce4710ee51f6",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 14,
            "noOfShots": 5,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T15:54:44.000000Z",
            "endTime": "2026-07-12T16:03:13.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "T",
            "isFairWayLeft": "F",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.2967097,
            "pinLong": 11.3835138,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2955156,
                    "startLong": 11.3791147,
                    "endLat": 49.2959951,
                    "endLong": 11.3811758,
                    "distance": 159.122,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:54:44.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "f9b4d2f9-65b2-4e22-9280-afe5485314a5",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2959951,
                    "startLong": 11.3811758,
                    "endLat": 49.2966671,
                    "endLong": 11.3826412,
                    "distance": 130.179,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T15:58:40.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "1d869e70-1057-486f-9d6c-643fce23f6aa",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.2966671,
                    "startLong": 11.3826412,
                    "endLat": 49.29665,
                    "endLong": 11.3833712,
                    "distance": 53.1315,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:01:15.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "25ca5017-c863-45e3-b8ac-ca938c2ccca9",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.29665,
                    "startLong": 11.3833712,
                    "endLat": 49.296706738331,
                    "endLong": 11.383506725711,
                    "distance": 11.7043,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:03:12.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "4108a819-6289-4d86-8154-3c5b14cf4e71",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.296706738331,
                    "startLong": 11.383506725711,
                    "endLat": 49.2967097,
                    "endLong": 11.3835138,
                    "distance": 0.610952,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:03:13.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "4525df25-6a5f-476c-980c-a3bdf6f523f1",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 15,
            "noOfShots": 6,
            "isGir": "T",
            "putts": 4,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T16:11:08.000000Z",
            "endTime": "2026-07-12T16:18:39.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.298124188786,
            "pinLong": 11.389528445904,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2976271,
                    "startLong": 11.3853761,
                    "endLat": 49.297506,
                    "endLong": 11.3880653,
                    "distance": 196.062,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:11:08.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "e76e9796-c29b-4c94-bc0d-8e401f2db620",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.297506,
                    "startLong": 11.3880653,
                    "endLat": 49.297912913682,
                    "endLong": 11.389551311731,
                    "distance": 117.176,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:15:25.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "be32c941-8a6c-4f56-825c-03a669870595",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.297912913682,
                    "startLong": 11.389551311731,
                    "endLat": 49.2979537,
                    "endLong": 11.3894709,
                    "distance": 7.40157,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:16:43.500000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "9f434e17-fac6-4630-a955-93de414de9da",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2979537,
                    "startLong": 11.3894709,
                    "endLat": 49.298105449427,
                    "endLong": 11.389522120697,
                    "distance": 17.2832,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:18:02.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "650abc4b-0fb6-4e83-9035-7cf37ec1fa6e",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.298105449427,
                    "startLong": 11.389522120697,
                    "endLat": 49.2981188,
                    "endLong": 11.3895269,
                    "distance": 1.52494,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:18:22.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "86e1043c-f923-4eac-b835-11209d80e666",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2981188,
                    "startLong": 11.3895269,
                    "endLat": 49.298124188786,
                    "endLong": 11.389528445904,
                    "distance": 0.609773,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:18:39.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "494dada4-0803-4fdf-8b10-037ea1d8737b",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 16,
            "noOfShots": 5,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T16:23:50.000000Z",
            "endTime": "2026-07-12T16:27:37.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 2,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.296936611834,
            "pinLong": 11.390207530348,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 9,
                    "clubId": 16,
                    "startLat": 49.2974893,
                    "startLong": 11.3911764,
                    "endLat": 49.297135323611,
                    "endLong": 11.390343158333,
                    "distance": 72.2697,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:23:50.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "488bf022-7bb7-4c1e-8649-2a671b6f23c3",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 56,
                    "clubId": 8,
                    "startLat": 49.297135323611,
                    "startLong": 11.390343158333,
                    "endLat": 49.2969385,
                    "endLong": 11.39023,
                    "distance": 23.3861,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:26:24.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 1,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7d01dc3e-47ee-42f0-b66a-8e613e3499d4",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2969385,
                    "startLong": 11.39023,
                    "endLat": 49.296937312464,
                    "endLong": 11.390215868018,
                    "distance": 1.03635,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:27:36.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "fa7f474b-c0d3-4119-9725-74701465fe62",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.296937312464,
                    "startLong": 11.390215868018,
                    "endLat": 49.296936611834,
                    "endLong": 11.390207530348,
                    "distance": 0.611433,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:27:37.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "38a4a4f2-2bf1-4684-ad4c-e216a7a28f50",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 17,
            "noOfShots": 7,
            "isGir": "F",
            "putts": 4,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T16:32:05.000000Z",
            "endTime": "2026-07-12T16:38:44.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "F",
            "isFairWayRight": "F",
            "isFairWayLeft": "T",
            "approachShotId": 3,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.297851361433,
            "pinLong": 11.390458962021,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2972153,
                    "startLong": 11.3886327,
                    "endLat": 49.2972911,
                    "endLong": 11.3897663,
                    "distance": 82.8826,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:32:05.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7e067729-8824-4a58-8a56-b3b6a871c207",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 11,
                    "clubId": 18,
                    "startLat": 49.2972911,
                    "startLong": 11.3897663,
                    "endLat": 49.297590852543,
                    "endLong": 11.390458233654,
                    "distance": 60.3677,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:35:52.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "006a97c1-02b9-4166-ad49-6fa9a51d3956",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 56,
                    "clubId": 8,
                    "startLat": 49.297590852543,
                    "startLong": 11.390458233654,
                    "endLat": 49.2977136,
                    "endLong": 11.390418,
                    "distance": 13.9616,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:37:05.500000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "e5e946a3-6bc6-4fe5-9d55-662958d7658a",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.2977136,
                    "startLong": 11.390418,
                    "endLat": 49.297832524335,
                    "endLong": 11.39045336098,
                    "distance": 13.474,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:38:19.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "c320dae7-4a4c-49ec-bbda-cc396be3e251",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.297832524335,
                    "startLong": 11.39045336098,
                    "endLat": 49.297845979405,
                    "endLong": 11.390457361723,
                    "distance": 1.52444,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:38:42.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "653328e7-72a2-4c08-b11e-ecff20d76b3a",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 1,
                    "startLat": 49.297845979405,
                    "startLong": 11.390457361723,
                    "endLat": 49.297845979405,
                    "endLong": 11.390457361723,
                    "distance": 1.15668e-10,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:38:43.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "8d797cd0-71e8-499a-8c65-0f9ff46d9407",
                    "tourQuality": null
                },
                {
                    "shotId": 7,
                    "clubType": 12,
                    "clubId": 1,
                    "startLat": 49.297845979405,
                    "startLong": 11.390457361723,
                    "endLat": 49.297851361433,
                    "endLong": 11.390458962021,
                    "distance": 0.609777,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:38:44.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "c8658dcb-f7ec-43e8-8f83-d0213290a642",
                    "tourQuality": null
                }
            ]
        },
        {
            "holeId": 18,
            "noOfShots": 7,
            "isGir": "F",
            "putts": 2,
            "isSandSaveChance": "F",
            "isSandSave": "F",
            "startTime": "2026-07-12T16:44:42.000000Z",
            "endTime": "2026-07-12T16:57:40.000000Z",
            "shouldIgnore": "F",
            "isFairWay": "T",
            "isFairWayRight": "F",
            "isFairWayLeft": "F",
            "approachShotId": 5,
            "isUpDownChance": "F",
            "isUpDown": "F",
            "isFairWayUser": "F",
            "isFairWayRightUser": "F",
            "isFairWayLeftUser": "F",
            "pinLat": 49.300296973397,
            "pinLong": 11.393669441102,
            "scoreOverride": null,
            "shots": [
                {
                    "shotId": 1,
                    "clubType": 1,
                    "clubId": 1,
                    "startLat": 49.2985664,
                    "startLong": 11.3891915,
                    "endLat": 49.2985359,
                    "endLong": 11.3910485,
                    "distance": 135.109,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:44:42.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "ecb4092b-245a-4f86-86fa-70f541e26489",
                    "tourQuality": null
                },
                {
                    "shotId": 2,
                    "clubType": 8,
                    "clubId": 15,
                    "startLat": 49.2985359,
                    "startLong": 11.3910485,
                    "endLat": 49.2988945,
                    "endLong": 11.3924364,
                    "distance": 108.539,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:48:16.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "567707ab-e639-4151-9f48-2099b03f5f7b",
                    "tourQuality": null
                },
                {
                    "shotId": 3,
                    "clubType": 9,
                    "clubId": 16,
                    "startLat": 49.2988945,
                    "startLong": 11.3924364,
                    "endLat": 49.2997805,
                    "endLong": 11.3928828,
                    "distance": 103.748,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:52:09.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "93f845dd-fe43-41e7-9022-4259a2c0b385",
                    "tourQuality": null
                },
                {
                    "shotId": 4,
                    "clubType": 10,
                    "clubId": 17,
                    "startLat": 49.2997805,
                    "startLong": 11.3928828,
                    "endLat": 49.3001152,
                    "endLong": 11.3936061,
                    "distance": 64.4443,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:54:02.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "d6362e18-ba21-46c9-97d7-73d74074c26a",
                    "tourQuality": null
                },
                {
                    "shotId": 5,
                    "clubType": 49,
                    "clubId": 19,
                    "startLat": 49.3001152,
                    "startLong": 11.3936061,
                    "endLat": 49.300298,
                    "endLong": 11.3936904,
                    "distance": 21.2346,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:56:34.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "6aaa40f8-599b-4ed2-af5b-2ffa01ebb856",
                    "tourQuality": null
                },
                {
                    "shotId": 6,
                    "clubType": 12,
                    "clubId": 20,
                    "startLat": 49.300298,
                    "startLong": 11.3936904,
                    "endLat": 49.300297384039,
                    "endLong": 11.393677824661,
                    "distance": 0.917177,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:57:39.000000Z",
                    "shouldIgnore": "F",
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "0b8332d0-562e-4ff0-9246-90af5a2fe5d2",
                    "tourQuality": null
                },
                {
                    "shotId": 7,
                    "clubType": 12,
                    "clubId": 1,
                    "startLat": 49.300297384039,
                    "startLong": 11.393677824661,
                    "endLat": 49.300296973397,
                    "endLong": 11.393669441102,
                    "distance": 0.611452,
                    "isHalfSwing": null,
                    "startAltitude": null,
                    "endAltitude": null,
                    "shotTime": "2026-07-12T16:57:40.000000Z",
                    "shouldIgnore": null,
                    "noOfPenalties": 0,
                    "isSandUser": null,
                    "isNonSandUser": null,
                    "shouldConsiderPuttAsChip": "F",
                    "userStartTerrainOverride": 0,
                    "shotUUID": "7facb9cd-74bd-43cb-a129-20de0935558c",
                    "tourQuality": null
                }
            ]
        }
    ],
    "ballMakeId": 16,
    "ballModelId": 59,
    "courseLocaleName": {
        "en": "Golfclub Herrnhof"
    },
    "notes": null
}`

