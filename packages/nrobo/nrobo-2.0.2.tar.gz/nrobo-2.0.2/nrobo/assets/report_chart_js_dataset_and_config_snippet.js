
                var labels_init = ["Passed", "Skipped", "Failed", "Errors", "Expected Failures", "Unexpected Passes", "Reruns"];
                var data_init   = [];
                var colors_init = [
                                    'rgb(0, 153, 115)',
                                    'rgb(255, 163, 58)',
                                    'rgb(250, 99, 132)',
                                    'rgb(255, 99, 132)',
                                    'rgb(255, 163, 58)',
                                    'rgb(250, 99, 132)',
                                    'rgb(255, 163, 58)'
                ]

                const data = {
                        labels: [
                            'Passed',
                            'Skipped',
                            'Failed',
                            'Errors',
                            'Expected Failures',
                            'Unexpected Passes',
                            'Reruns'
                        ],
                        datasets: [
                                    {
                                        label: 'Spherobot Test Run Result',
                                        data: [],
                                        backgroundColor: [
                                            'rgb(0, 153, 115)',
                                            'rgb(255, 163, 58)',
                                            'rgb(250, 99, 132)',
                                            'rgb(255, 99, 132)',
                                            'rgb(255, 163, 58)',
                                            'rgb(250, 99, 132)',
                                            'rgb(255, 163, 58)'
                                        ],
                                        circumference: 180,
                                        radius: '100%',
                                        offset: '2',
                                        rotation: 270,
                                        borderWidth: 1,
                                        hoverOffset: 4
                                    }
                                ]
                };


            const config = {
                type: 'doughnut',
                //type: 'pie',
                data: data,
            };


            // === include 'setup' then 'config' above ===

            var myChart = new Chart(
                document.getElementById('spherobot_result_chart'),
                config
            );
