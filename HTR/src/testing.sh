for file in ../../Results/Tests/Images/*; do
    filename=$(basename "$file")
    # running file and outputting it to raw_output.dump file
    python3 main.py --img_file "$file" > raw_output.dump
    # cleaning output
    result=$(grep '^Recognized:' raw_output.dump |  sed -n 's/.*"\([^"]*\)".*/\1/p')
    prob=$(grep -m 1 '^Probability:' raw_output.dump | awk '{print $2}')
    echo \"$result\" > cut_output.dump
    echo $prob >> cut_output.dump
    python3 testing.py $filename
done

rm *.dump


#  PLEASE NOTE
#  
#  This script will append the results.csv and does not have any way of knowing
#  the current working model. That is something that will be defined manually.
#
#  With this, incase the script isn't run from start to finish
#  you should remove any changes made on the temp csv before substituiting to the fixed one!