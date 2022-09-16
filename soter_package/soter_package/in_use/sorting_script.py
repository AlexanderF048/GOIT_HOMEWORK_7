def main():
    from pathlib import Path
    import sys
    import shutil 
    import os

    def path_check():
        

        if len(sys.argv) == 1:                      
            try_input=input("Please, input path to 'UNSORTED' directory::::")
            
            if os.path.exists(try_input) and Path(try_input).is_dir():
                returned_path=Path(fr"{try_input}")
                print(returned_path,'>>>>argument were taken from "INPUT 1"<<<<')
            else:
                print("Recursive check compleated.")
                returned_path=path_check()
         
        elif len(sys.argv) > 1:
            
            if os.path.exists(sys.argv[1])and Path(sys.argv[1]).is_dir():
                returned_path=Path(fr"{sys.argv[1]}")
                print('>>>>argument were taken from "TERMINAL ARGS"<<<<')
            else:
                print("Paht not exists")
                while True:
                    try_input=input("Please, input path to 'UNSORTED' directory::::")
                    if os.path.exists(try_input) and Path(try_input).is_dir():
                        returned_path=Path(fr"{try_input}")
                        print(returned_path,'>>>>argument were taken from "INPUT 2"<<<<')
                        break
          

                
  
        return returned_path

    def cleaner(directory):
        for trash in directory.iterdir():
            try:
                if trash.is_dir():
                    cleaner(trash)
                    trash.rmdir()
            except OSError:
                    continue
        return #print("Directory was cleaned.")           
    
    def translate(name_file):
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = (
            "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n",
            "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "",
            "e", "yu", "ya", "je", "i", "ji", "g"
              )
        TRANS = {}
    
        for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()
            translated=name_file.translate(TRANS)
        return translated
    
    def normalize(name_file):
        import re
        normalize = re.sub(r"[^\w]", "_", translate(name_file))
        return normalize.strip()

    def sort_this_dir(PATH):
    
        list_pictures=[]
        list_video=[]
        list_documents=[]
        list_music=[]
        list_archives=[]
        list_directory=[]
        list_unknown_type=[]
    
        categories={
            "Pictures":list_pictures,
            "Video":list_video, 
            "Documents":list_documents, 
            "Music":list_music, 
            "Archives":list_archives, 
            "UNKNOWN file type":list_unknown_type, 
            "Was found directory(es)": list_directory 
            }
        
        #в дальнейшем добавить возможность добавления форматов через аргументы в консоли
        pic_type=[".jpeg",".png",".jpg",".svg",".bmp"]    
        vid_type=[".avi",".mp4",".mov",".mkv"]
        doc_type=[".doc",".docx",".txt",".pdf",".xlsx",".pptx"]
        mus_type=[".mp3",".ogg",".wav",".amr"]
        arc_type=[".zip",".gz",".tar"] #NO RAR TYPE FILES
        
        #Если заменить внешний PATH_TO_UNSORTED на передаваемый PATH - при вызове рекурсии он будет работать внутри своих директорий.
        pic_dir=Path(PATH_TO_UNSORTED.joinpath("pictures"))
        vid_dir=Path(PATH_TO_UNSORTED.joinpath("video"))
        doc_dir=Path(PATH_TO_UNSORTED.joinpath("documents"))
        mus_dir=Path(PATH_TO_UNSORTED.joinpath("audio"))
        arc_dir=Path(PATH_TO_UNSORTED.joinpath("archives"))
        nft_dir=Path(PATH_TO_UNSORTED.joinpath("unknown_type_files"))
    
        if PATH.is_dir():
            
    
            for item in PATH.iterdir():
                ### можно пройтись через : for path in p.glob('*.txt'):
    
                if item.suffix in pic_type:                
                    list_pictures.append(item.name)               
                    if not pic_dir.is_dir():                                      
                        pic_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", pic_dir)                
                    #elif pic_dir.is_dir()==True: =======>>>> не преемлимо (==True / False )
                        #print("! DIRECTORY ALREADY EXISTS:", pic_dir)
                    #REPLACE
                    item=item.replace(pic_dir.joinpath(item.name))
                    #print("Removed item:",item)
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
                    
                    
    
                elif item.suffix in vid_type:                
                    list_video.append(item.name)                
                    if not vid_dir.is_dir():                                        
                        vid_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", vid_dir)                
                    #elif vid_dir.is_dir()==True:                    
                       # print("! DIRECTORY ALREADY EXISTS:", vid_dir) 
                    #REPLACE
                    item=item.replace(vid_dir.joinpath(item.name))
                    #print("Removed item:",item)
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
    
                elif item.suffix in doc_type:                
                    list_documents.append(item.name)               
                    if not doc_dir.is_dir():                                        
                        doc_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", doc_dir)                
                    #elif doc_dir.is_dir()==True:                    
                        #print("! DIRECTORY ALREADY EXISTS:", doc_dir) 
                    #REPLACE
                    item=item.replace(doc_dir.joinpath(item.name))
                    #print("Removed item:",item) 
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
    
                elif item.suffix in mus_type:               
                    list_music.append(item.name)              
                    if not mus_dir.is_dir():                                        
                        mus_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", mus_dir)                
                    #elif mus_dir.is_dir()==True:                    
                        #print("! DIRECTORY ALREADY EXISTS:", mus_dir) 
                    #REPLACE
                    item=item.replace(mus_dir.joinpath(item.name))
                    #print("Removed item:",item) 
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
    
                elif item.suffix in arc_type:                            
                     
                    list_archives.append(item.name) 
                    if not arc_dir.is_dir():                                        
                        arc_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", arc_dir)                
                    #elif arc_dir.is_dir()==True:                    
                        #print("! DIRECTORY ALREADY EXISTS:", arc_dir)
                    
                    #REPLACE CREATE UNDERDIR AND UNPUCK!
                    item=item.replace(arc_dir.joinpath(item.name))
                    #print("Removed item:",item) 
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
                    
                    unpuck_arc_dir=arc_dir.joinpath(item.stem)
                    unpuck_arc_dir.mkdir(parents = True, exist_ok =True)#### OUTPUT NONE
                    shutil.unpack_archive(item, unpuck_arc_dir)
                    
                    for unpucked in unpuck_arc_dir.iterdir():
                        normalized_unpucked=(normalize(unpucked.stem))+unpucked.suffix
                        unpucked=unpucked.rename((unpucked.parent).joinpath(normalized_unpucked))
                    
                    
    
                elif item.is_dir():
                    if item.is_dir()!= pic_dir or vid_dir or doc_dir or mus_dir or arc_dir or nft_dir:
                        list_directory.append(item.name)
                        sort_this_dir(item) #РЕКУРСИВНЫЙ ВЫЗОВ
                    else:
                        continue
               
               
                #UNKNOWN
                else:
                    list_unknown_type.append(item.name)               
    
                    if not nft_dir.is_dir():                                        
                        nft_dir.mkdir(parents = True, exist_ok =True)
                        #print("! DIRECTORY WAS CREATED:", nft_dir)
                    #elif nft_dir.is_dir()==True:                    
                        #print("! DIRECTORY ALREADY EXISTS:", nft_dir) 
                    #REPLACE
                    item=item.replace(nft_dir.joinpath(item.name))
                    #print("Removed item:",item) 
                    normalized_item=(normalize(item.stem))+item.suffix
                    item=item.rename((item.parent).joinpath(normalized_item))
            
            #######################CLEANER#################################
            
            cleaner(PATH)
            
            ###############################################################               
                                                        
        else:
            return print("..........Sorry, you specified a non-existent path. Please try again...........")
        ################# FORMATED REPORT OUTPUT ##########################            
        for cat, obj in categories.items():        
            print("|{:*^120}|".format(cat))
            counter=0
            for o in obj:
                counter+=1
                print("|{:^4}|{:<115}|".format(counter,o)) 
        print("|{:_^120}|".format("_"))                        
        ################################################################### 
     
    PATH_TO_UNSORTED=path_check()
    sort_this_dir(PATH_TO_UNSORTED)
    
    ################# FORMATED POSITION OUTPUT ########################
    print("|{:-^120}|".format("-")) 
    print("|{:^120}|".format("At the moment, location of yours'UNSORTED' directory is:"))
    print("|{:^120}|".format(f">>>  {PATH_TO_UNSORTED}  <<<"))
    print("|{:-^120}|".format("-")) 
    ###################################################################   
    
if __name__ == '__main__':  
    exit(main())
