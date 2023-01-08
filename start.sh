if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hacker-Jr-TG/kgfQ.git /kgfQ
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /kgfQ
fi
cd /kgfQ 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
