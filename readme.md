get_byteArr(file_obj)
파일을 0~256 숫자들의 배열로 변환

get_fileSize(byteArr)
파일의 크기(바이트) 반환

get_freqList(byteArr, fileSize)
숫자의 갯수를 파일 크기로 나눈 소수값으로 이루어진 배열 반환

get_entropy(freqList)
파일의 엔트로피 반환 (=<8.0)

get_highest_freq(freqList)
파일에서 가장 많이 노출된 문자 반환

get_front_charList(byteArr, highfreq)
파일에서 가장 많이 노출된 문자의 앞문자와 가장 많이 노출된 문자 반환(순위는 안넣음)

목표 get_front_charList_Rank(byteArr, ArrSet)
파일에서 가장 많이 노출된 문자의 앞문자와 가장 많이 노출된 문자의 순위 반환



all(file_name)

클래스 형태
  info.byteArr
  info.fileSize
  info.freqList
  info.entropy
  info.highfreq
  
