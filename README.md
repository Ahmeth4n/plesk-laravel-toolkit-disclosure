# Plesk Laravel Toolkit - Disclosure of All Domains on the Server

It has the domainId value of the "domain" parameter in the SSH Public Key Generator endpoint of the Laravel Toolkit plugin developed for Plesk. If the domainId you have given here belongs to a domain authorized by your user, it will return you a public key. But if you do not have authority on this domain and domainId matches a domain, you

```
{"status":"error","msg":"Failed to get public key for the domain 'testdomain.com': The user does not have access to domain \"testdomain.com."}
```

returns a response. Information disclosure starts right here. This disclosure allows you to list all domains on that server by enumerate the domainId parameter. The response shouldn't have shown us that it belongs to **testdomain.com**.

