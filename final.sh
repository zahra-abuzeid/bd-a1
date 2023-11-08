echo "INSIDE BASH WOOO"
container_id="bdacddfeedd8"
container_dir="/home/doc-bd-a1"
local_dir="bd-a1"

mkdir -p $local_dir/service-result


files_to_copy=("eda-in-1.txt" "eda-in-2.txt" "eda-in-3.txt" "k.txt" "res_dpre.csv" "vis.png")


for file in "${files_to_copy[@]}"; do
  docker cp $container_id:$container_dir/$file $local_dir/service-result/
done


docker stop $container_id

echo "Files copied to $local_dir/service-result. Container closed."
