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