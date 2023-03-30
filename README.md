# HDR-SCVC-Templating

This repository contains code to help optimize HDR templates based on doses delivered to reference points, as well as several example data sets based on various combinations of prescription and cylinder diameter.

## Code Inputs:
 - A set of ideal doses for the relevant reference points
 - A set of weights representing the relative priority of each reference point
 - A matrix representing the doses received by each reference point when only one dwell point is active at a time.
   - Each dwell point has its own row in the matrix, and the values in that row are the doses delivered to each reference point by just that dwell point. 
   - Each reference point has its own column, and the values in that column are the doses delivered to that reference point by each individual dwell point.
 
## Code Outputs:
 - The dwell times that best reproduce the ideal doses
 - The actual doses produced by these dwell times
 
# Templating Workflow:
  - Copy a data file, clearing the values from it
  - Create a blank brachytherapy plan in Eclipse to serve as the new template
    - Add the applicator(s)
      - Specify the dwell positions, but leave the dwell times all at 0 seconds for now
    - Create any reference points/lines that are relevant for template evaluation
      - For each point, identify ideal dose values, i.e. based on older templates, or based on dose goals from RTOG etc.
        - Write them all down as a vector, stored in the data file as "ideal_doses"
  -	For each dwell point, temporarily set its dwell time to 100 seconds (to reduce rounding effects), and set the dwell times of all other dwell points to 0 seconds
    - Record the dose delivered to each relevant reference point in a row of the "dwell_matrix" array in the data file
  - For each reference point, assign a numerical weight to it
    - Write all the weights down in a vector, stored in the data file as "weights"
  - Run the code
    - If the resulting doses aren’t good enough, change the target doses or the weights
  -	Put those dwell times back into Eclipse
  - The template is ready!
