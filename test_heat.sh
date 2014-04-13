STACK_NAME=x$1
#STACK_TEMPLATE=$2

if [[ -z $STACK_NAME ]]; then
    exit 1;
fi

heat stack-create -f heat/ponytest_stack.yml $STACK_NAME

function getStackStatus () {
    heat stack-show $STACK_NAME | grep "stack_status " | awk -F"|" '{print $3}' | sed -e 's/^ //'
}

while [ `getStackStatus` == "CREATE_IN_PROGRESS" ]; do
    echo "Polling for status in 60 seconds...";
    sleep 60;
    echo `getStackStatus`
done
