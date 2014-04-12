STACK_NAME=x$1
#STACK_TEMPLATE=$2

if [[ -z $STACK_NAME ]]; then
    exit 1;
fi

heat stack-create -f heat/ponytest_stack.yml $STACK_NAME

function getStackStatus () {
    heat stack-show $STACK_NAME | grep "stack_status " | awk -F"|" '{print $3}' | sed -e 's/^ //'
}

sleep 20;

status=`getStackStatus`

sleep 20; 

while [ `getStackStatus` == "CREATE_IN_PROGRESS" ]; do
    echo `getStackStatus`;
    sleep 20;
done

echo `getStackStatus`;

