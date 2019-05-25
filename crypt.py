def crypto(message,offset,offsetlis):  
        messagelis = []
        for i in message:
                messagelis.append(i)
        for i in range(len(messagelis)):
                cursor = offsetlis[i]
                cursor2 = messagelis[i]
                pos = i
        
                while pos > 0 and offsetlis[pos - 1] > cursor:
                        
                        offsetlis[pos] = offsetlis[pos - 1]
                        messagelis[pos] = messagelis[pos - 1]
                        pos = pos - 1
                        
                offsetlis[pos] = cursor
                messagelis[pos] = cursor2
        message = ''
        for item in messagelis:
                message = message + item
        e = 0
        message = message
        offset = offset
        decryption = "" 

        for letter in message:

                num = offset[e]
                num = int(num)
                ascii = ord(letter)
                newascii = ascii - num
                if newascii < 40:
                        newascii = newascii + 86
                nletter = chr(newascii)
                decryption = decryption + nletter
                e = e + 1
        return decryption
