# When Am I Getting Paid?

This is a simple web app I created to not only tell WUSTL DBBS students when they are getting paid, but also generate an internet calendar file (`.ics`) to add to their personal calendar.

General Web App Mechanism:

```mermaid
flowchart TD

A(Scrape WUSTL Finance Site for Payroll PDF File) --> B(Clean Up & Reformat Data to Tabular Format) 
B --> C(Generate Calendar from Tabular Data)
B --> D(Convert Dates Into Integers & Sort Smallest to Largest)
D --> E(Find Closest 'Greater' Date in Array to Current Date)
```
