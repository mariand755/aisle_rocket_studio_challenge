## Automated Test for Aisle Rocket Studios

This test suite covers Caeserstone Design & Gladiator Garage landing pages.


   1. Launches the landing page of Caeserstone Design
         - Asserts the Mission Statement is displayed.

   2. View the "Design for Life" section - Durable option
         - Click to open Durable option.
         - Asserts text on Durable option.
         - Closes Durable option.

   3. Launches the US Homepage of Gladiator Garage
         - Asserts the Mission Statement is displayed.

   4. View the Promotion Deals
         - Asserts the Promotion Bar is displayed
         - Asserts the Current Deals displayed under Bar
         - Collapse Promotion Bar


## How to Run the Test Suite

   1. `cd` into project.
   2. Activate virtual environment `source venv/bin/activate`.
   3. Run the tests for Caeserstone with `venv/bin/python3 -m unittest test_script.cs_landingpage_test`.
   4. Run the tests for Gladiator Garage with `venv/bin/python3 -m unittest test_script.gg_homepage_test`.
