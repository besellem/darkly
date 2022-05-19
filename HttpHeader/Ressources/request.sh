curl -s 'http://192.168.56.101/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \
	-H 'User-Agent: ft_bornToSec' \
	-H 'Referer: https://www.nsa.gov/' > saved.html

echo -n "flag : "
cat saved.html | grep flag | cut -d " " -f 7 | head -c 64
echo
