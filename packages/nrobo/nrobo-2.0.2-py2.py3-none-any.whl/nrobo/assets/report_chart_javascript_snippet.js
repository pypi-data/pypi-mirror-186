
        var temp=function(){ return 1;};
        if( window.onload )
        {
            //override "placeholder" with whatever already exists in onload
            temp = window.onload;
        }
        window.onload=function(){ set_onclick_event_on_filter_checkboxes(); temp();};

        function set_onclick_event_on_filter_checkboxes(){
            // Get all checkboxes
            checkboxes = document.getElementsByName("filter_checkbox");
            for(var counter=0; counter<checkboxes.length; counter++){
                checkboxes[counter].setAttribute('onClick', "spherobot_click(this)");
            }
        }

        var statuses = ["true", "true", "true", "true", "true", "true", "true"]
        var label_data_classes = ["passed", "skipped" , "failed", "error", "xfailed", "xpassed", "rerun"];

        var labels_after = [];
        var data_after = [];

        function spherobot_click(ele){

            // Get all checkboxes
            checkboxes = document.getElementsByName("filter_checkbox");

            // Remove chart data
            for(var counter=0; counter <checkboxes.length; counter++){
                checkboxes[counter].setAttribute('status', statuses[counter])
                removeData(myChart);
            }

            // Get class of clicked element
            class_of_clicked_element = ele.getAttribute("data-test-result") ;

            // Reset labels and data after click
            var labels_after = [];
            var data_after = [];
            var colors_after = [];

            //Loop through each checkbox
            for(var i=0, j=0; i< checkboxes.length; i++){

                //alert(labels_after[i]);
                //alert(data_after[i]);
                //alert(ele.getAttribute("data-test-result") + "<>" + checkboxes[i].getAttribute("data-test-result") + "\n" + checkboxes[i].getAttribute("status"));

                if(class_of_clicked_element !== checkboxes[i].getAttribute("data-test-result")
                    && checkboxes[i].getAttribute("status") === "true"){
                    //alert("INSIDE IF\n" + ele.getAttribute("data-test-result") + "<>" + checkboxes[i].getAttribute("data-test-result") + "\n" + checkboxes[i].getAttribute("status"));

                    labels_after[j] = labels_init[i];
                    data_after[j] = data_init[i];
                    colors_after[j] = colors_init[i];
                    j++;
                    //alert("Inside IF");

                } else if(class_of_clicked_element === checkboxes[i].getAttribute("data-test-result")
                    && checkboxes[i].getAttribute("status") === "false"){
                    //alert("INSIDE ELSE IF\n" + ele.getAttribute("data-test-result") + "<>" + checkboxes[i].getAttribute("data-test-result") + "\n" + checkboxes[i].getAttribute("status"));
                    checkboxes[i].setAttribute("status", "true");
                    statuses[i] = "true";
                    labels_after[j] = labels_init[i];
                    data_after[j] = data_init[i];
                    colors_after[j] = colors_init[i];
                    j++;

                    //alert("Inside ELSE IF");
                } else {
                    //alert("INSIDE ELSE\n" + ele.getAttribute("data-test-result") + "<>" + checkboxes[i].getAttribute("data-test-result") + "\n" + checkboxes[i].getAttribute("status"));
                    checkboxes[i].setAttribute("status", "false");
                    statuses[i] = "false";
                    //alert("INSIDE ELSE HI " + ele.getAttribute("data-test-result") + "<>" + checkboxes[i].getAttribute("data-test-result") + "\n" + checkboxes[i].getAttribute("checked"));
                }


            } // End of for


            // Add data and labels and update chart
            for(var counter=0; counter<labels_after.length; counter++){
                addData(myChart, labels_after[counter], data_after[counter], colors_after[counter] );
            }

        }


        function addData(chart, label, data, color) {
            chart.data.labels.push(label);
            chart.data.datasets.forEach((dataset) => {
                dataset.data.push(data);
                //dataset.backgroundColor.push(colors);
            });
            chart.data.datasets.forEach((dataset) => {
                //dataset.data.push(data);
                dataset.backgroundColor.push(color);
            });
            chart.update();
        }

        function removeData(chart) {
            chart.data.labels.pop();
            chart.data.datasets.forEach((dataset) => {
                dataset.data.pop();
            });
            chart.data.datasets.forEach((dataset) => {
                dataset.backgroundColor.pop();
            });
            chart.update();
        }
