# Retornar arquivo binário como download no Odoo

Tags: odoo, python
Category: Coding

O código abaixo pode ser usado em situações em que temos um arquivo binário ou anexo e desejamos que o mesmo seja retornado para o browser como um download.

### Download de campo Binary

Para download do conteúdo de um campo binário, devemos montar a URL a seguir:

```python
# module_name - the name of the model with the Binary field
# field_name - the name of the Binary field
# object_id - id of the record containing particular file.
# field_filename - name of a Char field containing file's name (optional).

base_url = self.env['ir.config_parameter'].get_param('web.base.url')

url = f'{base_url}/web/content?model=<module_name>&field=<field_name>&filename_field=<field_filename>&id=<object_id>'

return {
    'type': 'ir.actions.act_url',
    'url': file_url,
    'target': 'new'
}
```

### Download de anexo

Para download do conteúdo de um anexo, devemos montar a URL a seguir:

```python
import base64
# output is where you have the content of your file, it can be
# any type of content
output 
# encode
result = base64.b64encode(output.read())

# get base url
base_url = self.env['ir.config_parameter'].get_param('web.base.url')

# create attachment
attachment_id = self.env['ir.attachment'].create(
	{'name': "name", 'datas_fname': 'name.file_ext', 'datas': result})

# prepare download url
download_url = f'{base_url}/web/content/{str(attachment_id.id)}?download=true'

# download
return {
	"type": "ir.actions.act_url",
	"url": download_url,
	"target": "new",
}
```

### Fontes:

- [https://www.odoo.com/pt_BR/forum/ajuda-1/download-binary-file-directly-203828](https://www.odoo.com/pt_BR/forum/ajuda-1/download-binary-file-directly-203828)
- [https://dirtyhandsphp.blogspot.com/2017/06/odoo-download-binary-file-in-v10.html](https://dirtyhandsphp.blogspot.com/2017/06/odoo-download-binary-file-in-v10.html)