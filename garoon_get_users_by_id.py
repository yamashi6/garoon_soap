from zeep import Client
from zeep import xsd

client = Client(wsdl='https://(サブドメイン名).cybozu.com/g/index.csp?WSDL')

header = xsd.ComplexType([
                xsd.Element('Action', xsd.String()),
                xsd.Element('Security', 
                    xsd.ComplexType([xsd.Element(
                        'UsernameToken',
                        xsd.ComplexType([
                            xsd.Element('Username', xsd.String()),
                            xsd.Element('Password', xsd.String()),
                        ])
                    )]
                )),

                xsd.Element('Timestamp', 
                    xsd.ComplexType([
                        xsd.Element('Created', xsd.String()),
                        xsd.Element('Expires', xsd.String()),
                    ])
                ),

                xsd.Element('Locale', xsd.String()),
            ])

header_value = header(
        Action="BaseGetUsersById", 
        Security={'UsernameToken':{'Username':'','Password':''}}, 
        Timestamp={'Created':'2010-08-12T14:45:00Z','Expires':'2037-08-12T14:45:00Z'},
        Locale="jp")

request_data  = {
    'parameters': {'user_id':[3, 4, 5]}
}
try:
    response = client.service.BaseGetUsersById(**request_data, _soapheaders=[header_value])
except:
    import traceback
    traceback.print_exc()