rule creds_re{
        meta:
            description = "Test sample yara rule"
        strings:
            $s = "http://attacker.com"
        condition:
            $s
}