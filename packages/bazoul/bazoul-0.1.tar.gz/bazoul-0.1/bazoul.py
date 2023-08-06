from rabk import rabk

rabk = rabk('templates')

template_name = 'invoice'
context = {'name': 'John Doe', 'amount': '100'}
rabk.print_bill(template_name, context)
