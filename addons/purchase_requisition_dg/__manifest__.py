{
    "name": "Purchase requisition Desiteg",
    "maintainer": "Desiteg",
    "depends": [
        "base",
        "report",
        "purchase",
        'barcodes',
        'mail',
        # 'sale_stock'
    ],
    'summary': 'Manage Purchase requisition Desiteg',
    "application": True,
    'description': """
        Requisición de compra
        ==============================================
    """,
    'website': 'https://es.wikipedia.org/wiki/Requisici%C3%B3n_de_compra',
    "images": ["img/requisicion.png"],
    "data": [
        "views/views.xml",
        "report/account_invoice_report_view.xml",
        "data/sequence.xml",
        'data/mail_template_payment_data.xml',
    ],
    "css": [
        "css/index.css"
    ],
    "version": "0.1",
    'auto_install': True,
}
