window.onload = function () {
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["CNCI", "PLEK", "CPC2", "CPPred", "lgc", "CPAT", "LncADeep", "GFStack"],
            datasets: [
                {
                    label: '200',
                    data: [41.018, 4.177, 0.778, 4.865, 0.219, 1.498, 183.489, 19.991],
                    backgroundColor: [
                        // 'rgba(255, 206, 86, 0.2)',
                        // 'rgba(75, 192, 192, 0.2)'
                        'rgba(226, 160, 165)'

                    ]
                }, {
                    label: '1000',
                    data: [138.575, 8.232, 1.150, 22.761, 0.855, 2.904, 352.090, 70.760],
                    backgroundColor: [
                        'rgba(137, 188, 195)'
                    ]
                }, {
                    label: '2000',
                    data: [155.667, 14.569, 2.017, 44.840, 1.625, 5.214, 489.328, 142.324],
                    backgroundColor: [
                        'rgba(240, 196, 124)'
                    ]
                }, {
                    label: '5000',
                    data: [380.590, 33.130, 5.152, 110.678, 3.792, 12.840, 896.839, 348.154],
                    backgroundColor: [
                        'rgba(175, 201, 135)'
                    ]
                }, {
                    label: '10000',
                    data: [707.453, 64.881, 9.363, 220.688, 7.729, 27.614, 1573.938, 719.336],
                    backgroundColor: [
                        'rgba(127, 104, 167)'
                    ]
                }
            ]
        }
    },

    );

    var ctx2 = document.getElementById("myChart2").getContext('2d');
    var myChart2 = new Chart(ctx2, {
        type: 'radar',
        data: {
            labels: ["AUC", "F1", "MCC", "ACC", "P", "R", "Spec"],
            datasets: [
                {
                    label: 'CNCI',
                    data: [0.871, 0.818, 0.732, 0.858, 0.705, 0.976, 0.800],
                    borderColor: [
                        // 'rgba(255, 206, 86, 0.2)',
                        // 'rgba(75, 192, 192, 0.2)'
                        'rgba(57, 70, 135)'

                    ],
                    backgroundColor: [
                        'rgba(57, 70, 135,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'PLEK',
                    data: [0.891, 0.726, 0.585, 0.768, 0.593, 0.935, 0.687],
                    borderColor: [
                        'rgba(69, 155, 149)'
                    ],
                    backgroundColor: [
                        'rgba(69, 155, 149,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPC2',
                    data: [0.897, 0.735, 0.601, 0.778, 0.603, 0.942, 0.698],
                    borderColor: [
                        'rgba(240, 196, 124)'
                    ],
                    backgroundColor: [
                        'rgba(240, 196, 124,0.1)',

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPPred',
                    data: [0.808, 0.727, 0.593, 0.763, 0.584, 0.965, 0.664],
                    borderColor: [
                        'rgba(175, 201, 135)'
                    ],
                    backgroundColor: [
                        'rgba(175, 201, 135,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'lgc',
                    data: [0.854, 0.700, 0.541, 0.741, 0.564, 0.923, 0.652],
                    borderColor: [
                        'rgba(127, 104, 167)'
                    ],
                    backgroundColor: [
                        'rgba(127, 104, 167,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPAT',
                    data: [0.947, 0.835, 0.752, 0.882, 0.767, 0.917, 0.866],
                    borderColor: [
                        'rgba(226, 160, 165)'
                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'LncADeep',
                    data: [0.987, 0.932, 0.899, 0.953, 0.891, 0.978, 0.942],
                    borderColor: [
                        'rgba(128, 164, 165)'
                    ],
                    backgroundColor: [
                        'rgba(128, 164, 165,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'GFStack',
                    data: [0.992, 0.942, 0.913, 0.967, 0.940, 0.943, 0.971],
                    borderColor: [
                        'rgba(203, 65, 59)'
                    ],
                    backgroundColor: [
                        'rgba(203, 65, 59,0.1)'

                    ],
                    borderWidth: 2
                }
            ]
        }

    },

    );



    var ctx3 = document.getElementById("myChart3").getContext('2d');
    var myChart3 = new Chart(ctx3, {
        type: 'radar',
        data: {
            labels: ["AUC", "F1", "MCC", "ACC", "P", "R", "Spec"],
            datasets: [
                {
                    label: 'CNCI',
                    data: [0.891, 0.753, 0.695, 0.861, 0.615, 0.969, 0.830],
                    borderColor: [
                        // 'rgba(255, 206, 86, 0.2)',
                        // 'rgba(75, 192, 192, 0.2)'
                        'rgba(57, 70, 135)'

                    ],
                    backgroundColor: [
                        'rgba(57, 70, 135,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'PLEK',
                    data: [0.953, 0.574, 0.461, 0.707, 0.420, 0.906, 0.652],
                    borderColor: [
                        'rgba(69, 155, 149)'
                    ],
                    backgroundColor: [
                        'rgba(69, 155, 149,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPC2',
                    data: [0.910, 0.657, 0.574, 0.784, 0.504, 0.943, 0.740],
                    borderColor: [
                        'rgba(240, 196, 124)'
                    ],
                    backgroundColor: [
                        'rgba(240, 196, 124,0.1)',

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPPred',
                    data: [0.838, 0.638, 0.557, 0.758, 0.475, 0.971, 0.698],
                    borderColor: [
                        'rgba(175, 201, 135)'
                    ],
                    backgroundColor: [
                        'rgba(175, 201, 135,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'lgc',
                    data: [0.870, 0.615, 0.518, 0.745, 0.460, 0.928, 0.694],
                    borderColor: [
                        'rgba(127, 104, 167)'
                    ],
                    backgroundColor: [
                        'rgba(127, 104, 167,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'CPAT',
                    data: [0.952, 0.789, 0.731, 0.894, 0.696, 0.910, 0.889],
                    borderColor: [
                        'rgba(226, 160, 165)'
                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'LncADeep',
                    data: [0.984, 0.895, 0.865, 0.951, 0.840, 0.956, 0.949],
                    borderColor: [
                        'rgba(128, 164, 165)'
                    ],
                    backgroundColor: [
                        'rgba(128, 164, 165,0.1)'

                    ],
                    borderWidth: 2
                }, {
                    label: 'GFStack',
                    data: [0.975, 0.851, 0.851, 0.932, 0.820, 0.885, 0.945],
                    borderColor: [
                        'rgba(203, 65, 59)'
                    ],
                    backgroundColor: [
                        'rgba(203, 65, 59,0.1)'

                    ],
                    borderWidth: 2
                }
            ]
        }
    },

    );
    // var ctx3 = document.getElementById("myChart3").getContext('2d');
    // var myChart3 = new Chart(ctx3, {
    //     type: 'line',
    //     data: {
    //         labels: ["1", "5", "10"],
    //         datasets: [
    //             {
    //                 label: 'lncADeep',
    //                 data: [1573, 2260, 2798],
    //                 borderColor: [
    //                     // 'rgba(255, 206, 86, 0.2)',
    //                     // 'rgba(75, 192, 192, 0.2)'
    //                     'rgba(226, 160, 165)'

    //                 ],
    //                 backgroundColor: [
    //                     'rgba(226, 160, 165,0.1)'

    //                 ],
    //                 borderWidth: 3
    //             }, {
    //                 label: 'lgc',
    //                 data: [7.72, 8.14, 8.57],
    //                 borderColor: [
    //                     'rgba(137, 188, 195)'
    //                 ],
    //                 backgroundColor: [
    //                     'rgba(137, 188, 195,0.1)'

    //                 ],
    //                 borderWidth: 3
    //             }
    //         ]
    //     },
    //     options: {
    //         scales: {
    //             yAxes: [{
    //                 ticks: {
    //                     beginAtZero: true
    //                 }
    //             }]
    //         }
    //     }
    // },

    // );


    var ctx4 = document.getElementById("c_cnci").getContext('2d');
    var myChart = new Chart(ctx4, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [41.018, 138.575, 155.667, 380.590, 707.453],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        }
    },

    );

    var ctx5 = document.getElementById("c_plek").getContext('2d');
    var myChart = new Chart(ctx5, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [4.177, 8.232, 14.569, 33.130, 64.881],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    },

    );
    var ctx11 = document.getElementById("c_cpc2").getContext('2d');
    var myChart = new Chart(ctx11, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'CPC2',
                    data: [0.778, 1.150, 2.017, 5.152, 9.363],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        }
    },

    );
    var ctx6 = document.getElementById("c_cppred").getContext('2d');
    var myChart = new Chart(ctx6, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'cppred',
                    data: [4.865, 22.761, 44.840, 110.678, 20.688],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        }
    },

    );
    var ctx7 = document.getElementById("c_lgc").getContext('2d');
    var myChart = new Chart(ctx7, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [0.219, 0.855, 1.625, 3.792, 7.729],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    },

    );

    var ctx8 = document.getElementById("c_cpat").getContext('2d');
    var myChart = new Chart(ctx8, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [1.498, 2.904, 5.214, 12.840, 27.614],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    },

    );

    var ctx9 = document.getElementById("c_lncadeep").getContext('2d');
    var myChart = new Chart(ctx9, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [183.489, 352.090, 489.328, 896.839, 1573.938],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    },

    );

    var ctx10 = document.getElementById("c_gfstack").getContext('2d');
    var myChart = new Chart(ctx10, {
        type: 'line',
        data: {
            labels: ["200", "1000", "2000", "5000", "10000"],
            datasets: [
                {
                    label: 'lncADeep',
                    data: [19.991, 70.760, 142.324, 348.154, 719.336],
                    borderColor: [
                        'rgba(226, 160, 165)'

                    ],
                    backgroundColor: [
                        'rgba(226, 160, 165,0.1)'

                    ],
                    borderWidth: 3
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    },

    );
};


