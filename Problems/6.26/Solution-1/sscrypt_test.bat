@echo off

echo == Run Encryption with Key Mn=[89,243,21,150,245], and string is "10101" ==
python sscrypt.py -e 89 243 212 150 245 10101

echo "Press any key to continue next test... "
pause

echo == Run Decryption with super increasing sequencer Rn=[3,11,24,50,115], Pair A/B =113/250, and S is 546
python sscrypt.py -d 3 11 24 50 115 113 250 546

echo "Press any key to continue next test... "
pause
echo == Run Verification with super increasing sequencer Rn=[3,11,24,50,115], Pair A/B =113/250
python sscrypt.py -v 3 11 24 50 115 113 250