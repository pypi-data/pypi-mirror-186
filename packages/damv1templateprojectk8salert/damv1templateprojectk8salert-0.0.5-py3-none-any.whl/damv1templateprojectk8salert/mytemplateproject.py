from enum import Enum

class displayed(Enum):
    ## Compailer design template = https://onecompiler.com/html
    tmplt_evrntwrapper = f'''
<en-note>
<h1 style="margin:0; padding:0;">{{value_str_ervnt_rptname}}</h1>
<h2 style="margin-bottom:40px; margin-top:0; padding:0;">Contex id : {{value_str_contexid}}</h2>
{{value_strlst_grplines}}
<div style="margin-top:45px;">
  <p style="color:Gray;">&#9899; :: DAM2022 | Power Commerce Asia</p>
</div>
</en-note>
'''

    tmplt_evrntwrapper_v2 = f'''
<en-note>
<h1 style="margin:0; padding:0;">{{value_str_ervnt_rptname}}</h1>
<h2 style="margin-bottom:40px; margin-top:0; padding:0;">Contex id : {{value_str_contexid}}</h2>
{{value_strlst_grplines}}
{{value_strlst_another_1}}
<div style="margin-top:45px;">
  <p style="color:Gray;">&#9899; :: DAM2022 | Power Commerce Asia</p>
</div>
</en-note>
'''

    tmplt_evrntgrpLines = f'''
&#128308;<p style="margin:0; padding:0;color:MediumSeaGreen;font-size:18px;display:inline;line-height:10px;">({{value_str_number}})</p><h3 style="margin:0; padding:0;display:inline;line-height:10px;"> :: {{value_str_ns}} :: {{value_str_po}} | {{value_str_cont}}</h3>
<div style='margin-left:25px;padding-bottom:8px;'>
  <p style="margin:0;padding:0;color:{{value_str_color_status}};font-size:16px;line-height:10px">Status [{{value_str_status}}] :: Restart[{{value_str_restart}}] :: Age {{value_str_age}}</p>
</div>
{{value_str_lstlines}}
<p style="margin-bottom:10px;"></p>
'''

    tmplt_evrntgrpAnother1 = f'''
<div style="margin-top:45px;">
  <p>Test text in another-1</p>
</div>
'''

    tmplt_evrntLines = f'''
<div style='margin-left:25px;'>
  <p style="margin:0; padding-top:0;color:red">RETRIEVE A RECORD [ {{value_str_patterns}} ][ last {{value_str_sincelast}} ][ head n 1 ] :</p>
  <p style="margin:0; padding-top:0;">{{value_str_line}}</p>
</div>
'''
    tmplt_telemsg = f'''
\U00002757*{{value_str_messagename}}*
Context id \: ||{{value_str_contextid}}||
Start Date Time \: {{value_str_StartDateTime7}}

The list of detected object \({{value_str_count_dtect_obj}}\) on {{value_str_ns}}\:
  \-\| ``{{value_str_dtect_obj}}``

\U00002B55[REPORT]({{value_str_url_shareable}})
Note: All the data reports in evernote will be deleted after 2 days
'''
    tmplt_telemsg_str_dtect_obj = f'''{{value_str_obj}} \-\-\> restart\: {{value_obj_restart}} age\: {{value_obj_age}}'''