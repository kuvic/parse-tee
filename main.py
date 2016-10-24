import re
import urllib.request
import urllib.parse

def getPage(url):
    '''Function that fakes a Mozilla and gets the page and decodes
    from ISO 8859 7'''

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = None
    headers = {'User-Agent': user_agent}

    req = urllib.request.Request(url, values, headers)
    
    f = urllib.request.urlopen(req)
    return (f.read().decode('iso-8859-7'))

def returnlines(text_list, key):
    '''return lines containing the key'''
    result = []
    for line in text_list:
        if key in line:
            result.append(line)
    del result[0]
    return result

def returninfo(mlist):
    ## match link with a ref <a(.*?)>
    ## match other two texts <font class(.*?)<
    p_link = re.compile('<a(.*?)>')
    p_text = re.compile('<font class(.*?)<')
    result = []
    for match in mlist:
        #print (match)
        link_list = p_link.findall(match)
        text_list = p_text.findall(match)
        try:
            link = link_list[0]
        except:
            link = "No link available"
        org = text_list[0]
        body = text_list[1]
        print (link,org,body,sep='\n')

#        match = match.split('<')
#        if len(match)>7:
#            #print (match)
#            link = match[2].split('\"')[1].strip()
#            org = match[3].split('>')[1].strip()
#            body = match[7].split('>')[1].strip()
#            result.append([org,body,link])
    return result

strings = '''<TD vAlign="top" style="padding:16px 16px 0px 16px;" width="100%"><font class="titleorimageid16244557siteid467">ΥΠΟΥΡΓΕΙΟ ΠΕΡΙΒΑΛΛΟΝΤΟΣ &amp; ΕΝΕΡΓΕΙΑΣ</font><BR><font class="descriptionid16244557siteid467">ΑΝΑΘΕΣΗ:&quot;Μ1:Υδατικό διαμέρισμα Δυτικής Πεόποννήσου (GR 01)Βόρειας Πελοποννήσου (GR 02) και Ανατολικής Πελοποννήσου (GR 03)&quot;Ημερομηνία Ανάρτησης 4.9.2016</font>&nbsp;</TD></TR>
<TR ALIGN="LEFT">
<TD vAlign="top" style="padding:6px 16px 0px 16px;" width="100%"><a href="http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis/KTHMATOLOGIO1.pdf" target="p_target=_blank"><font class="titleorimageid16244557siteid467">ΕΘΝΙΚΟ ΚΤΗΜΑΤΟΛΟΓΙΟ ΚΑΙ ΧΑΡΤΟΓΡΑΦΗΣΗ Α.Ε.</font></a><BR><font class="descriptionid16244557siteid467">«Μελέτη Β’ Φάσης Κτηματογράφησης &amp; Υποστηρικτικών Υπηρεσιών για τη δημιουργία Εθνικού Κτηματολογίου στην Δημοτική Κοινότητα Λαμιαίων της Δημοτικής Ενότητας Λαμιαίων του Δήμου Λαμιαίων της Περιφερειακής Ενότητας Φθιώτιδος, και στη Δημοτική Κοινότητα Λεβαδέων της Δημοτικής Ενότητας Λεβαδέων του Δήμου Λεβαδέων της Περιφερειακής Ενότητας Βοιωτίας» και κωδικό ΚΤ4-03 Ημερομηνία Ανάρτησης 6.10.2016</font>&nbsp;</TD></TR>
<TR ALIGN="LEFT">
<TD vAlign="top" style="padding:6px 16px 0px 16px;" width="100%"><a href="http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis/KTHMATOLOGIO2.pdf" target="p_target=_blank"><font class="titleorimageid16244557siteid467">ΕΘΝΙΚΟ ΚΤΗΜΑΤΟΛΟΓΙΟ ΚΑΙ ΧΑΡΤΟΓΡΑΦΗΣΗ Α.Ε.</font></a><BR><font class="descriptionid16244557siteid467"> «Μελέτη Β’ Φάσης Κτηματογράφησης &amp; Υποστηρικτικών Υπηρεσιών για τη δημιουργία Εθνικού Κτηματολογίου στην Δημοτική Κοινότητα Βόλου της Δημοτικής Ενότητας Βόλου του Δήμου Βόλου της Περιφερειακής Ενότητας Μαγνησίας» και κωδικό ΚΤ4-02 Ημερομηνία Ανάρτησης 6.10.2016</font>&nbsp;</TD></TR>
<TR ALIGN="LEFT">
<TD vAlign="top" style="padding:6px 16px 0px 16px;" width="100%"><a href="http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis/KTHMATOLOGIO3.pdf" target="p_target=_blank"><font class="titleorimageid16244557siteid467">ΕΘΝΙΚΟ ΚΤΗΜΑΤΟΛΟΓΙΟ ΚΑΙ ΧΑΡΤΟΓΡΑΦΗΣΗ Α.Ε.</font></a><BR><font class="descriptionid16244557siteid467">«Μελέτη Β’ Φάσης Κτηματογράφησης &amp; Υποστηρικτικών Υπηρεσιών για τη δημιουργία Εθνικού Κτηματολογίου στο Δήμο Αθηναίων της Περιφερειακής Ενότητας Κεντρικού Τομέα Αθηνών» και κωδικό ΚΤ4-01,Ημερομηνία Ανάρτησης 6.10.2016</font>&nbsp;</TD></TR>
<TR ALIGN="LEFT">
<TD vAlign="top" style="padding:6px 16px 0px 16px;" width="100%"><a href="http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis/YPOURGEIO%20PERIBALONTOS%20ENERGEIAS.pdf1.pdf" target="p_target=_blank"><font class="titleorimageid16244557siteid467">ΥΠΟΥΡΓΕΙΟ ΠΕΡΙΒΑΛΛΟΝΤΟΣ &amp; ΕΝΕΡΓΕΙΑΣ</font></a><BR><font class="descriptionid16244557siteid467">ΑΝΑΘΕΣΗ: Κατάρτιση 1ης Αναθεώρησης Σχεδίων Διαχείρισης Λεκανών Απορροής Ποταμών των 14 Υδατικών Διαμερισμάτων της χώρας, σύμφωνα με τις προδιαγραφές της Οδηγίας 2000/60/ΕΚ, κατ’ εφαρμογή του Ν. 3199/2003 όπως τροποποιήθηκε και ισχύει και του ΠΔ 51/2007 (επτά μελέτες) για τη Μ.7 : «Υδατικό Διαμέρισμα Νήσων Αιγαίου (GR 14)»Ημερομηνία Ανάρτησης 7.10.2016</font>&nbsp;</TD></TR>
<TR ALIGN="LEFT">
<TD vAlign="top" style="padding:6px 16px 0px 16px;" width="100%"><a href="http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis/YPOURGEIO%20PERIBALONTOS%20ENERGEIAS.pdf2.pdf" target="p_target=_blank"><font class="titleorimageid16244557siteid467">ΥΠΟΥΡΓΕΙΟ ΠΕΡΙΒΑΛΛΟΝΤΟΣ &amp; ΕΝΕΡΓΕΙΑΣ</font></a><BR><font class="descriptionid16244557siteid467">ΑΝΑΘΕΣΗ: M6 Υδατικό Διαμέρισμα Κρήτης (GR 13)του έργου &quot;Κατάρτιση 1Η΅Αναθεώρησης Σχεδίων Διαχείρησης Λεκανών Απορροής Ποταμών των 14 Υδατικών Διαμερισμάτων της Χώρας&quot;Ημερομηνία Ανάρτησης 7.10.2016</font>&nbsp;</TD></TR>
<TR>'''

link_pat = re.compile(r'<a\shref="(.+?)"')

# siteid467">ΥΠΟΥΡΓΕΙΟ ΠΕΡΙΒΑΛΛΟΝΤΟΣ &amp; ΕΝΕΡΓΕΙΑΣ</font>
title_pat = re.compile(r'siteid467">(.+?)<')

url = "http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis"
key = 'descriptionid16244557siteid467'
page = getPage(url).split('\n')
match_lines = returnlines(page,key)
#m = returninfo(match_lines)

c = 0
for i in strings.split('\n'):
    if "siteid467" in i:
        print('line: ', c)
        c = c + 1

        link = re.findall(link_pat, i)
        try:
            print("LINK", link[0])
        except:
            print("no link ______________")
        texts = re.findall(title_pat, i)
        try:
            print("TITLE", texts[0])
            print("BODY ", texts[1])
        except:
            print("Problems in line", c-1)
