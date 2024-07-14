# Linkar URL externa a um menu

Tags: odoo, python
Category: Coding

Inicialmente, devemos criar uma action para url externa

```xml
<record id="external_link" model="ir.actions.act_url">
        <field name="name">Site Externo</field>
        <field name="type">ir.actions.act_url</field>
        <field name="target">new</field>
        <field name="url">http://blog.exemplo.com</field>
</record>
```

Em seguida linkamos a `act_url` a um `menu_item`:

```xml
<menuitem action="external_link" name="Odoobiz" id="menu_odoobiz_link" parent="website_blog.menu_website_blog_root"/>
```

### Fonte:

- [https://dirtyhandsphp.blogspot.com/2017/09/odoo-10-link-external-url-to-menu.html](https://dirtyhandsphp.blogspot.com/2017/09/odoo-10-link-external-url-to-menu.html)