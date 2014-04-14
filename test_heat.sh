GEN_NAME=$1
STACK_NAME=x${GEN_NAME}
HOST_NAME=h${GEN_NAME}
STACK_TEMPLATE=$2
IMAGE_NAME=$3

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
    IMAGE_NAME='';
fi

heat stack-create -f $STACK_TEMPLATE $STACK_NAME -P myhostname=${HOST_NAME};myimagename=${IMAGE_NAME}

function getStackStatus () {
    heat stack-show $STACK_NAME | grep "stack_status " | awk -F"|" '{print $3}' | sed -e 's/^ //'
}

while [ `getStackStatus` == "CREATE_IN_PROGRESS" ]; do
    echo "Polling for status in 60 seconds...";
    sleep 60;
    echo `getStackStatus`
done
