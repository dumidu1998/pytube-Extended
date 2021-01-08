#!/bin/sh
echo "Merging";
for f in *.mp4 
do
echo "$f"
#echo "${f%.mp4}"

	for aud in audio/*.mp4
	do
		echo "${aud#*audio/}"
		
	done
	if [ "${aud#*audio/}"=="$f" ]
	then
		echo "ddddddddddd"
		#ffmpeg -n -i "$f" -i "${aud}" -c:v copy -c:a copy "output/${f%.mp4}.mp4"
	fi
	 
	#rm "$f" 
done
