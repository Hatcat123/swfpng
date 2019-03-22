for x in *.swf; do
    swfrender ${x} -o ${x%.swf}.png
done