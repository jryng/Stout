# Stout for Raspberry Pi by jeffg
# If your Raspberry Pi is running something other than Raspbian, please run this script as sudo.

import cups
import time
import lcddriver


disp = lcddriver.lcd()

cups.setServer('localhost')  # Change this for your own CUPS server IP, if using to check on a remote instance.
ccon = cups.Connection()
genPrinter = ccon.getDefault()   # get status updates for whichever printer is defined as the server default in CUPS.

class printer:

    def state():

        mainstuff = ccon.getPrinterAttributes(str(genPrinter))
        return mainstuff['printer-state']
        
    def jobid():
    	
    	jobdict = ccon.getJobs()
    	jobls = jobdict.keys()
    	listobj = list(jobls)[0]
    	return listobj
        
    def jobinfo():
        
        attr = ccon.getJobAttributes(int(printer.jobid()))
        return attr

class display:

    def long_string(disp, text = '', num_line = 1, num_cols = 16):   # This portion is copied from demo_scrolling_text.py in the original lcd repo. Credit to Dídac García for writing the original code.
        if(len(text) > num_cols):
            disp.lcd_display_string(text[:num_cols],num_line)
            time.sleep(1)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                disp.lcd_display_string(text_to_print,num_line)
                time.sleep(0.2)
                
    def idle():
        disp.lcd_display_string('  Printer Idle  ', 1)
    
    def offline():
        disp.lcd_display_string(' General Error', 1)
        disp.lcd_display_string('CUPS OFFLINE?', 2)

    def final():
        disp.lcd_display_string('Rendering Done', 1)
        disp.lcd_display_string('Finalizing Print', 2)
        
    def printing():
        pgp = str(printer.jobinfo()['job-media-progress'])
        pgn = str(printer.jobinfo()['job-impressions-completed'])
        pn = str(printer.jobinfo()['job-name'])
        un = str(printer.jobinfo()['job-originating-user-name'])
        disp.lcd_display_string('{}% of page {}'.format(pgp, pgn), 2)
        display.long_string(disp, 'PRINTING: {} from {}'.format(pn, un), 1)
#        disp.lcd_display_string('NOW PRINTING', 1)			# Uncomment this line and comment out the one above if you'd prefer a simpler printer display.

        if pgp == '100':
           disp.lcd_clear()
           
while True:

   if printer.state() == 3:
      display.idle()
      time.sleep(1)
      disp.lcd_clear()
      
   else:
      display.printing()
      time.sleep(0.6) 
   

