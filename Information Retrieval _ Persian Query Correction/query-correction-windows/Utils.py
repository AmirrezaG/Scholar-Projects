import os
import xml.etree.ElementTree as ET
from Document import Document_Object
from tqdm import tqdm
import json
from InMemIndex import InMemIndex

scriptPath = os.getcwd()

def Build(Index: InMemIndex) -> None:

    loadFromJSON(Index, scriptPath+'\\resources\\DocumentStore.json')
    Index.buildVocab()
    Index.store2Disk(scriptPath+'\\resources\\Index.pickle')
    Index.store2DiskFreq(scriptPath+'\\resources\\FrequencyIndex.pickle')
    Index.store2DiskVocab(scriptPath+'\\resources\\VocabularyIndex.pickle')

def Load() -> InMemIndex:
    Index = InMemIndex()
    Index.loadFromDisk(scriptPath+'\\resources\\Index.pickle') 
    Index.loadFromDiskFreq(scriptPath+'\\resources\\FrequencyIndex.pickle')
    Index.loadFromDiskVocab(scriptPath+'\\resources\\VocabularyIndex.pickle')
    return Index


def FormatSuggestions(sugguestions:list, N:int) -> str:
    result = ''
    if sugguestions == None:
        return 'No result found'
    for i,item in enumerate(sugguestions):
        if i == N:
            break
        confidence = "{:.3f}".format(item[1]*100)
        result += f'sugguestions: {item[0]} --> confidence: {confidence}%\n'
        i += 1
    return result

def parseXML(path, count=-1):
    dict = {}
    if count == -1:
        print('Parsing XML as tree: ', end='')
        xml_tree = ET.parse(path)
        xml_root = xml_tree.getroot()
        print('Done')

        print('Get tree lenght: ', end='')
        lenght = 0
        for item in xml_root.iter('doc'):
            lenght += 1
        print('Done')

        xml_root = xml_tree.getroot()
        cnt = 0
        for item in tqdm(xml_root.iter('doc'), desc='Parsing XML file', total=lenght ):
            dict[cnt] = [item[0].text, item[1].text, item[2].text]
            cnt += 1
    
    elif count > 0:
        print('Parsing XML as tree: ', end='')
        xml_tree = ET.parse(path)
        xml_root = xml_tree.getroot()
        print('Done')

        print('Get tree lenght: ', end='')
        lenght = 0
        for item in xml_root.iter('doc'):
            lenght += 1
        print('Done')

        xml_root = xml_tree.getroot()
        cnt = 0
        for item in tqdm(xml_root.iter('doc'), desc='Parsing XML file', totoal=lenght):
            if cnt >= count:
                break
            dict[cnt] = [item[0].text, item[1].text, item[2].text]
            cnt += 1

    return dict


def loadFromJSON(Index: InMemIndex ,path):
        with open(path, 'r', encoding='utf8') as jsonFile:
            print('Parsing JSON file: ', end='')
            jsonDict = json.loads(jsonFile.read())
            print('Done')
            docList = []
            for id in tqdm(jsonDict, desc='Building Index from JSON file'):
                abstract = jsonDict[id]['abstract']
                if abstract == None:
                    abstract = ''
                doc = Document_Object(int(id), jsonDict[id]['title'], jsonDict[id]['url'], abstract)
                Index.addDoc(doc)
            

#def add2DB(parsedXML, db, strt , end, dbNum):
#    for item in tqdm(range(strt, end), desc='Saving parsed xml to DB'):
#        doc = Document_Object(item, parsedXML[item][0], parsedXML[item][1], parsedXML[item][2])
#        parsedXML.pop(item)
#        db[str(doc.id)] = pickle.dumps(doc)
#        print('Added doc[%6d] to DB%d' %item %dbNum)
#
#
#def inputXML2DB():
#    parsedXML = parseXML(scriptPath + '\\resources\\fawiki-latest-abstract.xml')
#    print("Parsed XML file.")
#    threads = []
#    dbs = []
#    start = 0
#    end = 0
#    max = len(parsedXML)
#    ratio = max // os.cpu_count() + 1
#    for i in range(os.cpu_count()):
#        dbs.append(dbm.open(scriptPath + f'\\resources\\Store\\tmp\\StoreDB{i}', 'c'))
#        end += ratio
#        if end > max:
#            end = max
#        print('registering thread %d' % i)
#        threads.append(Thread(target=add2DB, args=(parsedXML, dbs[i], start, end, i)))
#        start = end
#
#    for thread in threads:
#        thread.start()
#
#    for thread in threads:
#        thread.join()
#    
#    for db in dbs:
#        db.close()
#
#def mergeDBs():
#    data = {}
#    db = dbm.open(scriptPath + '\\resources\\Store\\StoreDB', 'w')
#    for i in range(os.cpu_count()):
#        dbi = dbm.open(scriptPath +  f'\\resources\\Store\\tmp\\StoreDB{i}', 'r')
#        for key in tqdm(dbi, desc='Reading docs from DB%d' %i):
#            print('Reading doc[%6d]' %int(key) )
#            data[int(key)] = pickle.loads(dbi[key])
#        dbi.close()
#        for key in tqdm(data, desc='Merging DB%d to DB' %i):
#            print('Merging doc[%6d]' %int(key) )
#            db[str(key)] = pickle.dumps(data[key])
#        data.clear()
#    db.close()
#
#
#def validateStore(store: Document_Store) -> None:
#    xmlDict = parseXML(scriptPath + '\\resources\\fawiki-latest-abstract.xml')
#    with open(scriptPath + '\\resources\\Log.txt', 'w') as log:
#        for doc in tqdm(xmlDict, desc='Validating DB'):
#            if xmlDict[doc][0] == store.Store[doc].title and  xmlDict[doc][1] == store.Store[doc].url and xmlDict[doc][2] == store.Store[doc].abstract:
#                continue
#            else:
#                log.write('Doc[%6d] is BAD\n' %doc)