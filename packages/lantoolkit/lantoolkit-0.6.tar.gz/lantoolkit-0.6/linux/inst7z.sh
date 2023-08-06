echo "Have you installed 7-zip?[y/n]"
echo -e "你安装过7zip么？ \c"
read answer
echo -e "请告诉我你的账户密码(你的数据不会被记录)： \c"
read pwd
if (($answer == "n"));then
	tar -jxvf p7z1602.tar.bz2
	cd p7zip_16.02
	echo $pwd | sudo -S make
	echo $pwd | sudo  -S make install
	cd ../
	rmdir p7zip_16.02
echo “Done!”