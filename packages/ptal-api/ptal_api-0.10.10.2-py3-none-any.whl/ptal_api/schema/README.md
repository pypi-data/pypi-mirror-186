To generate schema following commands should be run:

1. Get introspection (you can also get it from gitlab introspection job artifacts)
```bash
python3 -m sgqlc.introspection --exclude-deprecated -H "Authorization: Bearer <token>" <graphql url> introspection.json
```
**Note**: for now there is some bug in sgqlc, so we should change default value 
`"{performSynchronously:true}"` to `null` for correct schema generation
2. Generate code
```bash
sgqlc-codegen schema introspection.json api_schema.py
```
3. do not forget to comment/remove `import sgqlc.types.datetime` in `api_schema.py`.
4. add both `introspection.json` and `api_schema.py` files to commit
