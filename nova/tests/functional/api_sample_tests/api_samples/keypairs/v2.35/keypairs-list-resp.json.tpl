{
    "keypairs": [
        {
            "keypair": {
                "fingerprint": "%(fingerprint)s",
                "name": "%(keypair_name)s",
                "type": "%(keypair_type)s",
                "public_key": "%(public_key)s"
            }
        }
    ],
    "keypairs_links": [
        {
            "href": "%(versioned_compute_endpoint)s/keypairs?limit=1&marker=%(keypair_name)s",
            "rel": "next"
        }
    ]
}
