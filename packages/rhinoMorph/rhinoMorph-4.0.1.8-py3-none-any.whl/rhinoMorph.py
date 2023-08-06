import jpype
import os.path


def startRhino():
    '''RHINO를 시작한다'''
    filepath = os.path.dirname(os.path.realpath(__file__))
    classpath = os.path.join(os.path.abspath(filepath), 'rhinoMorph/lib/rhino.jar')
    print('filepath: ', filepath)
    print('classpath: ', classpath)

    if jpype.isJVMStarted():
        print("JVM is already started~")
    else:
        jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath, convertStrings=True)

    # rhino = jpype.JPackage('rhino')       # get the package
    # RHINO = rhino.RHINO                   # get the class
    # rn = RHINO()                          # create an instance of the class
    rn = jpype.JClass('rhino.RHINO')        # This line substitutes above 3 lines
    rn.ExternInit_forPython(filepath)       # Start RHINO

    if rn:
        print("RHINO started!")
    else:
        print("RHINO could not start!")

    return rn


def stringToList(files):
    '''문자열을 리스트로 만든다'''
    print(files)
    files_text = []
    for file in files:
        fileText = "";
        with open(file, mode="rt", encoding="utf=8") as f:
            data = f.readlines()  # 리스트
            s = ' '.join(data)  # 문자열
        fileText += s  # 모든 문자열을 하나로 합침
        files_text.append(fileText)  # 각 파일의 내용을 files_text[n] 으로 접근 가능
    return files_text


def wholeResult_2D(rn, input, xrVv=False):
    '''형태소 분석 결과를 Java의 2차원 배열 형태로 가지고 온다'''
    output = rn.ExternCall_forPython(input, xrVv)
    outputArr = rn.GetOutputPartArr_static(output)
    return outputArr


def makeComplexNNG(morphs, poses, eojul_idx):
    '''하나의 어절에서 NNG 또는 NNP 로 연결된 것을 하나의 NNG로 만든다'''
    new_morphs = []
    new_poses = []
    newidx = 0
    for idx in range(len(morphs)):
        if idx < newidx:
            continue

        if newidx < (len(morphs)):
            if poses[newidx] == 'NNG' or poses[newidx] == 'NNP':    # 현재가 명사형이면
                temp = morphs[newidx]
                t_idx = newidx

                cur_eojul_idx = eojul_idx[t_idx]                    # 현재의 배열 번호
                cnt = 0
                for t in range(t_idx + 1, len(morphs)):
                    if cur_eojul_idx == eojul_idx[t]:               # 현재의 배열번호와 다음의 배열번호가 같을 때만 (한 어절)
                        if poses[t] == 'NNG' or poses[t] == 'NNP':  # 다음도 명사형이면
                            temp += morphs[t]
                            cnt += 1
                        else:
                            break
                    else:
                        break

                new_morphs.append(temp)
                new_poses.append('NNG')
                newidx = newidx + cnt + 1

            else:
                new_morphs.append(morphs[newidx])
                new_poses.append(poses[newidx])
                newidx = newidx + 1

    return new_morphs, new_poses


def wholeResult_list(rn, input, pos=['all'], eomi=False, combineN=False, xrVv=False):
    '''형태소 분석 결과를 Python의 두 개 리스트(morph, pos)로 가지고 온다.
    1. rn: RHINO 객체
    2. input: 입력문
    3. pos: 선택할 품사. 기본값은 모든 품사
    4. eomi: 어말어미 부착 여부, 기본값은 부착없이 원형 사용
    5. combineN: True시 하나의 어절 내에서 연속된 NNG, NNP를 하나의 NNG로 연결한 뒤, morphs, poses 결과를 출력
    6. xrVv: XR+하 형태를 동사로 변환할 것인지 여부'''
    output = rn.ExternCall_forPython(input, xrVv)
    outputArr = rn.GetOutputPartArr_static(output)

    morphs = []; poses = []; eojul_idx = []     # ; eojul = []
    for outputPart in outputArr:
        # eojul.append(outputPart[0])           # 어절 형태
        morphs.append(outputPart[1])            # 각 형태소
        poses.append(outputPart[2])             # 각 형태소의 품사
        eojul_idx.append(outputPart[3])         # 어절의 인덱스

    # 한 어절 내에 있는 연속된 명사를 하나의 명사로 결합한다
    if combineN:
        morphs, poses = makeComplexNNG(morphs, poses, eojul_idx)

    # 일부 품사만 선택(pos=) 및 eomi=True의 처리
    if (pos[0] == 'all'):                       # 모든 품사를 선택하는 경우
        for idx in range(len(morphs)):
            if (eomi):
                if (poses[idx] in ['VV', 'VA', 'VX', 'VCP', 'VCN']):
                    morphs[idx] = morphs[idx] + '다'
    else:                                       # 일부 품사만 선택하는 경우
        morphs2 = []
        poses2 = []
        for idx in range(len(morphs)):
            if (eomi):
                if (poses[idx] in ['VV', 'VA', 'VX', 'VCP', 'VCN']):
                    morphs[idx] = morphs[idx] + '다'

            if poses[idx] in pos:               # 현재 형태소의 품사가 찾고자 하는 품사의 목록에 들어가 있으면
                morphs2.append(morphs[idx])     # 형태소 부분만 가져온다
                poses2.append(poses[idx])       # 품사 부분만 가져온다

    if pos[0] == 'all':
        return morphs, poses
    else:
        return morphs2, poses2


def wholeResult_text(rn, input, xrVv=False):
    '''형태소 분석 결과를 TEXT로 된 원 분석 결과 형태로 가지고 온다'''
    output = rn.ExternCall_forPython(input, xrVv)
    return output


def onlyMorph(rn, files_text, selectPOS, newSetences, xrVv=False):
    '''형태소 분석 결과를 Python의 리스트로 가지고 오되, 지정된 품사의 형태 부분만 가져온다
        1. rn: RHINO 객체
        2. files_text: 파일 텍스트
        3. selectPOS: 선택할 품사
        4. newSetences: 문자열 리스트
        5. xrVv: XR+하 형태를 동사로 변환할 것인지 여부'''
    for fileText in files_text:
        output = rn.ExternCall_forPython(fileText, xrVv)  # 형태소 분석
        outputArr = rn.GetOutputPartArr_static(output)           # 어절별로 분리

        selected = []
        for outputPart in outputArr:
            if outputPart[2] in selectPOS:          # 현재 어절이 해당 품사에 해당하면
                selected.append(outputPart[1])      # 그 어절의 형태소 부분만 저장
        morphSentence = ' '.join(selected)          # 분리된 형태소 문자열을 하나의 문자열로 합침
        newSetences.append(morphSentence)           # 합쳐진 형태소 문자열을 리스트에 입력
    return newSetences


def onlyMorph_list(rn, input, pos=['all'], eomi=False, combineN=False, xrVv=False):
    '''형태소 분석 결과를 Python의 리스트로 가지고 오되, 지정된 품사의 형태 부분만 가져온다
    1. rn: RHINO 객체
    2. input: 입력문
    3. pos: 선택할 품사. 기본값은 모든 품사
    4. eomi: 어말어미 부착 여부, 기본값은 부착없이 원형 사용
    5. combineN: True시 하나의 어절 내에서 연속된 NNG, NNP를 하나의 NNG로 연결한 뒤, morphs, poses 결과를 출력
    6. xrVv: XR+하 형태를 동사로 변환할 것인지 여부'''
    output = rn.ExternCall_forPython(input, xrVv)
    outputArr = rn.GetOutputPartArr_static(output)

    morphs = [] ; poses = [] ; eojul_idx = []
    for outputPart in outputArr:
        morphs.append(outputPart[1])            # 각 형태소
        poses.append(outputPart[2])             # 각 형태소의 품사
        eojul_idx.append(outputPart[3])         # 어절의 인덱스

    # 한 어절 내에 있는 연속된 명사를 하나의 명사로 결합한다
    if combineN:
        morphs, poses = makeComplexNNG(morphs, poses, eojul_idx)

    # 일부 품사만 선택(pos=) 및 eomi=True의 처리
    if(pos[0] == 'all'):                        # 모든 품사를 선택하는 경우
        for idx in range(len(morphs)):
            if (eomi):
                if (poses[idx] in ['VV', 'VA', 'VX', 'VCP', 'VCN']):
                    morphs[idx] = morphs[idx] + '다'
    else:                                       # 일부의 품사만 선택하는 경우
        morphs2 = []
        for idx in range(len(morphs)):
            if (eomi):
                if (poses[idx] in ['VV', 'VA', 'VX', 'VCP', 'VCN']):
                    morphs[idx] = morphs[idx] + '다'

            if poses[idx] in pos:               # 현재 형태소의 품사가 찾고자 하는 품사의 목록에 들어가 있으면
                morphs2.append(morphs[idx])     # 형태소 부분만 가져온다

    if pos[0] == 'all':
        return morphs
    else:
        return morphs2

