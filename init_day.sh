next_day=$(( `ls -d */ | egrep '^day[0-9]+/$' | wc -l` + 1 ))
dirNum=`printf "%02d" $next_day`
dir=day$dirNum
mkdir $dir ; touch $dir/part1.py $dir/part2.py
printf "import sys\nfile = open(f'{sys.path[0]}/input.txt', 'r')\n" | tee $dir/part1.py $dir/part2.py > /dev/null
bash ./get_input.sh $next_day
