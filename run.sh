# Run the python update and predict commands
# Create python virtual environment if it doesn't exist
if [ ! -d 'venv' ]; then
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
fi

# Run the python update and predict scripts
source venv/bin/activate
python update.py
python predict.py
deactivate

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
