for chrome
pytest -v -s -m "sanity" --html=./Reports/reports.html testCases/ --browser chrome 
REM pytest -v -s -m "sanity and regression" --html=./Reports/reports.html testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" --html=./Reports/reports.html testCases/ --browser chrome 
REM pytest -v -s -m "regression" --html=./Reports/reports.html testCases/ --browser chrome



for Edge
pytest -v -s -m "sanity" --html=./Reports/reports.html testCases/ --browser Edge
REM pytest -v -s -m "sanity and regression" --html=./Reports/reports.html testCases/ --browser Edge
REM pytest -v -s -m "sanity or regression" --html=./Reports/reports.html testCases/ --browser Edge 
REM pytest -v -s -m "regression" --html=./Reports/reports.html testCases/ --browser Edge