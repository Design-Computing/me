# 🛑🛑🛑 STOP! Don't run this yet! 🛑🛑🛑

cd ..
git clone https://github.com/Design-Computing/course.git
cd me
pip install -r ../course/requirements.txt
bash ../course/extensions.sh
python ../course/set1/tests.py

# Before you run this file, change these to be your name and email address, 
# then take the # off the value from just before the quote. 
# I.e. make #" int just "
git config --global user.email #"email@example.com"
git config --global user.name #"Ben Doherty"

# once you've done this, run this file by copying this command to the terminal:
# bash codespace_startup.sh 
