# S8 generated-distribution drift correction

GitHub CI correctly detected that three committed generated role ZIPs did not match the final canonical Protocol v3 source:

- `software-design.zip`
- `software-implementation.zip`
- `software-verification.zip`

`software-qualification.zip` already matched.

Root cause: the three stale ZIPs were produced from an earlier intermediate canonical snapshot during S8 reconstruction. This is a generated-artifact parity defect, not a protocol-semantic defect.

Correction: rebuild `dist/` with the checked-in `source/build_skills.py` against the exact branch canonical source and replace only the mismatched generated ZIPs. Required local checks after rebuilding:

```text
python source/check_protocol_semantics.py
python source/check_protocol_lifecycle_cases.py
python source/build_skills.py --output dist
python source/build_skills.py --output dist --check
```

Expected: all checks PASS. No protocol semantics, source doctrine, templates, role definitions, or version are changed by this correction.
