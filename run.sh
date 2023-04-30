# Run the python update and predict commands
python3 update.py
python3 predict.py

# Read the count from file
count=$(head -n 1 'counter.txt')

# Prepare the commit message
message='Update #'$count

# Update the count in file
count=$(($count + 1))
echo $count > 'counter.txt'

# Stage, commit and push the changes
git add .
git commit -m "$message"
git push
