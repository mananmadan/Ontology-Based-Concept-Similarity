#little magic
p=7;

for((m=1; m<=p; m++))
do
    for((n=1; n<=2; n++))
    do
      echo -ne "#";
    done
 if ((m<=4))
  then
    for((a=1;a<=m; a++))
    do
      echo -ne " ";
    done
fi
if ((m<=4))
 then
    for((i=1; i<=2; i++))
    do
      echo -ne "#";
    done
  fi
       for((j=0;j<=8-2*m; j=j+1))
       do
         echo -ne " ";
       done

   if ((m<=4))
    then
   for((i=1; i<=2; i++))
   do
     echo -ne "#";
   done
fi
   if ((m<=4))
    then
      for((a=1;a<=m; a++))
      do
        echo -ne " ";
      done
  fi
  if ((m>4))
   then
     for((a=0;a<=12; a++))
     do
       echo -ne " ";
     done
 fi

  for((i=1; i<=2; i++))
  do
    echo -ne "#";
  done

    echo;
done

pip install nltk
pip install pandas
pip install matplotlib
pip install networkx
python2 kntool/nltk_download.py
