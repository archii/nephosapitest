GEN_NAME=$1
STACK_NAME=x${GEN_NAME}
HOST_NAME=h${GEN_NAME}
STACK_TEMPLATE=$2
IMAGE_NAME=$3
CREATE_POLL_INTERVAL=60
DELETE_POLL_INTERVAL=10

USAGE="\n    Usage:\n    $0 BASE_NAME STACK_TEMPLATE [IMAGE_NAME]\n\n    BASE_NAME and STACK_TEMPLATE are required.\n"

if [[ -z $GEN_NAME ]]; then
    echo -e $USAGE;
    exit 1;
fi

if [[ -z $STACK_TEMPLATE ]]; then
    echo -e $USAGE;
    exit 1;
fi

if [[ -z $IMAGE_NAME ]]; then
    PARAMS="myhostname=${HOST_NAME}";
else
    PARAMS="myhostname=${HOST_NAME};myimagename=${IMAGE_NAME}";
fi

heat stack-create -f $STACK_TEMPLATE $STACK_NAME -P $PARAMS || exit 1

function stackExists () {
    heat stack-list -f name=${STACK_NAME}  | grep ${STACK_NAME} 
}

function getStackStatus () {
    heat stack-show $STACK_NAME | grep "stack_status " | awk -F"|" '{print $3}' | sed -e 's/^ //'
}

while [ `getStackStatus` == "CREATE_IN_PROGRESS" ]; do
    echo "Polling for status in ${CREATE_POLL_INTERVAL} seconds...";
    sleep ${CREATE_POLL_INTERVAL};
    echo `getStackStatus`
done

if [ `getStackStatus` == "CREATE_COMPLETE" ]; then
    echo `getStackStatus`
    echo "Tearing down stack after successful test..."
    heat stack-delete $STACK_NAME
fi

STACK_EXISTS=`stackExists`
if [[ -z "${STACK_EXISTS}" ]]; then
    echo "Stack ${STACK_NAME} is DELETED!"
    echo "Test complete!"
else
    STACK_STATUS=`getStackStatus`
    while [ "${STACK_STATUS}" == "DELETE_IN_PROGRESS" ]; do
        echo "Polling for DELETE status in ${DELETE_POLL_INTERVAL} seconds..."
        sleep ${DELETE_POLL_INTERVAL}
        echo `getStackStatus`
    done
fi
