#!/bin/sh
while getopts :n: opt
do
    case $opt in
        n)
            args_num=$(echo $OPTARG | awk -F "(:|@|://)" '{print NF}')
            if [ $args_num -eq 3 ]; then
                # 不含username, password
                proxy_protocol=$(echo $OPTARG | awk -F "(:|@|://)" '{print $1}')
                proxy_host=$(echo $OPTARG | awk -F "(:|@|://)" '{print $2}')
                proxy_port=$(echo $OPTARG | awk -F "(:|@|://)" '{print $3}')
            elif [ $args_num -eq 5 ]; then
                proxy_protocol=$(echo $OPTARG | awk -F "(:|@|://)" '{print $1}')
                proxy_user=$(echo $OPTARG | awk -F "(:|@|://)" '{print $2}')
                proxy_pass=$(echo $OPTARG | awk -F "(:|@|://)" '{print $3}')
                proxy_host=$(echo $OPTARG | awk -F "(:|@|://)" '{print $4}')
                proxy_port=$(echo $OPTARG | awk -F "(:|@|://)" '{print $5}')
            else
                echo "url is error"
                exit 1
            fi
            ;;
        *)
            ;;
    esac
done
shift "$((OPTIND-1))"
proxy_ip=$(getent hosts $proxy_host | head -n1 | cut -d " " -f1)
conf=/tmp/proxychains4.conf.$UID.$$
cat << EOF > $conf
strict_chain
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
EOF
echo $proxy_protocol $proxy_ip $proxy_port $proxy_user $proxy_pass >> $conf
trap "rm -f $conf" INT TERM
para="-q -f "${conf}" "${@}
proxychains4 $para
ec="$?"
rm -f "$conf"
exit "$ec"