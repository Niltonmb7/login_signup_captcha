# -*- coding: utf-8 -*-
{
    'name': 'Login/signup reCAPTCHA',
    'version': '1.0',
    'summary': """Login and signup with reCAPTCHA""",
    'description': """reCAPTCHA es un servicio gratuito que protege tu sitio del spam y los abusos. 
        Utiliza técnicas avanzadas de análisis de riesgos para diferenciar entre humanos y bots.
        reCAPTCHA v3 te ayuda a detectar el tráfico abusivo en tu sitio web sin que los usuarios 
        interactúen con él. En lugar de mostrar un desafío de CAPTCHA, reCAPTCHA v3 muestra una 
        puntuación para que puedas elegir la acción más adecuada para tu sitio web.""",
    'author': 'NXMB',
    'company': 'PNCM',
    'website': 'https://www.gob.pe/cunamas',
    'category': 'Extra Tools',
    'depends': ['base'],
    'license': 'LGPL-3',
    'depends': ['base','web'],
    'data': ['views/captcha_views.xml'],
    'installable': True,
    'auto_install': False,
}