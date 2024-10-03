#sequence
start=1
end=5
for i in $(seq $start $end)
do
  # file sys
  filename="file${i}.txt"
  if [ -f "$filename" ]; then
    # write to file
    echo "Appending to $filename"
    echo "We added this text" >> "$filename"
  else
    echo "Creating $filename"
    echo "This is a newly created file" > "$filename"
  fi
done
echo "Operation completed!"