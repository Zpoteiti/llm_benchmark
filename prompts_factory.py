# 测试提示词集合

# 系统提示词
SYSTEM_PROMPT = '''# null
Source: https://gofastmcp.com/changelog



<Update label="v2.10.6" description="2025-07-19">
  ## [v2.10.6: Hymn for the Weekend](https://github.com/jlowin/fastmcp/releases/tag/v2.10.6)

  A special Saturday release with many fixes.

  ## What's Changed

  ### Enhancements 🔧

  * Resolve #1139 -- Implement include\_context argument in Context.sample by [@codingjoe](https://github.com/codingjoe) in [#1141](https://github.com/jlowin/fastmcp/pull/1141)
  * feat(settings): add log level normalization by [@ka2048](https://github.com/ka2048) in [#1171](https://github.com/jlowin/fastmcp/pull/1171)
  * add server name to mounted server warnings by [@artificial-aidan](https://github.com/artificial-aidan) in [#1147](https://github.com/jlowin/fastmcp/pull/1147)
  * Add StatefulProxyClient by [@hopeful0](https://github.com/hopeful0) in [#1109](https://github.com/jlowin/fastmcp/pull/1109)

  ### Fixes 🐞

  * Fix OpenAPI empty parameters by [@FabrizioSandri](https://github.com/FabrizioSandri) in [#1128](https://github.com/jlowin/fastmcp/pull/1128)
  * Fix title field preservation in tool transformations by [@jlowin](https://github.com/jlowin) in [#1131](https://github.com/jlowin/fastmcp/pull/1131)
  * Fix optional parameter validation in OpenAPI integration by [@jlowin](https://github.com/jlowin) in [#1135](https://github.com/jlowin/fastmcp/pull/1135)
  * Do not silently exclude the "context" key from JSON body by [@melkamar](https://github.com/melkamar) in [#1153](https://github.com/jlowin/fastmcp/pull/1153)
  * Fix tool output schema generation to respect Pydantic serialization aliases by [@zzstoatzz](https://github.com/zzstoatzz) in [#1148](https://github.com/jlowin/fastmcp/pull/1148)
  * fix: \_replace\_ref\_with\_defs; ensure ref\_path is string by [@itaru2622](https://github.com/itaru2622) in [#1164](https://github.com/jlowin/fastmcp/pull/1164)
  * Fix nesting when making OpenAPI arrays and objects optional by [@melkamar](https://github.com/melkamar) in [#1178](https://github.com/jlowin/fastmcp/pull/1178)
  * Fix `mcp-json` output format to include server name by [@jlowin](https://github.com/jlowin) in [#1185](https://github.com/jlowin/fastmcp/pull/1185)
  * Only configure logging one time by [@jlowin](https://github.com/jlowin) in [#1187](https://github.com/jlowin/fastmcp/pull/1187)

  ### Docs 📚

  * Update changelog.mdx by [@jlowin](https://github.com/jlowin) in [#1127](https://github.com/jlowin/fastmcp/pull/1127)
  * Eunomia Authorization with native FastMCP's Middleware by [@tommitt](https://github.com/tommitt) in [#1144](https://github.com/jlowin/fastmcp/pull/1144)
  * update api ref for new `mdxify` version by [@zzstoatzz](https://github.com/zzstoatzz) in [#1182](https://github.com/jlowin/fastmcp/pull/1182)

  ### Other Changes 🦾

  * Expand empty parameter filtering and add comprehensive tests by [@jlowin](https://github.com/jlowin) in [#1129](https://github.com/jlowin/fastmcp/pull/1129)
  * Add no-commit-to-branch hook by [@zzstoatzz](https://github.com/zzstoatzz) in [#1149](https://github.com/jlowin/fastmcp/pull/1149)
  * Update README.md by [@jlowin](https://github.com/jlowin) in [#1165](https://github.com/jlowin/fastmcp/pull/1165)
  * skip on rate limit by [@zzstoatzz](https://github.com/zzstoatzz) in [#1183](https://github.com/jlowin/fastmcp/pull/1183)
  * Remove deprecated proxy creation by [@jlowin](https://github.com/jlowin) in [#1186](https://github.com/jlowin/fastmcp/pull/1186)
  * Separate integration tests from unit tests in CI by [@jlowin](https://github.com/jlowin) in [#1188](https://github.com/jlowin/fastmcp/pull/1188)

  ## New Contributors

  * [@FabrizioSandri](https://github.com/FabrizioSandri) made their first contribution in [#1128](https://github.com/jlowin/fastmcp/pull/1128)
  * [@melkamar](https://github.com/melkamar) made their first contribution in [#1153](https://github.com/jlowin/fastmcp/pull/1153)
  * [@codingjoe](https://github.com/codingjoe) made their first contribution in [#1141](https://github.com/jlowin/fastmcp/pull/1141)
  * [@itaru2622](https://github.com/itaru2622) made their first contribution in [#1164](https://github.com/jlowin/fastmcp/pull/1164)
  * [@ka2048](https://github.com/ka2048) made their first contribution in [#1171](https://github.com/jlowin/fastmcp/pull/1171)
  * [@artificial-aidan](https://github.com/artificial-aidan) made their first contribution in [#1147](https://github.com/jlowin/fastmcp/pull/1147)

  **Full Changelog**: [v2.10.5...v2.10.6](https://github.com/jlowin/fastmcp/compare/v2.10.5...v2.10.6)
</Update>

<Update label="v2.10.5" description="2025-07-11">
  ## [v2.10.5: Middle Management](https://github.com/jlowin/fastmcp/releases/tag/v2.10.5)

  A maintenance release focused on OpenAPI refinements and middleware fixes, plus console improvements.

  ## What's Changed

  ### Enhancements 🔧

  * Fix Claude Code CLI detection for npm global installations by [@jlowin](https://github.com/jlowin) in [#1106](https://github.com/jlowin/fastmcp/pull/1106)
  * Fix OpenAPI parameter name collisions with location suffixing by [@jlowin](https://github.com/jlowin) in [#1107](https://github.com/jlowin/fastmcp/pull/1107)
  * Add mirrored component support for proxy servers by [@jlowin](https://github.com/jlowin) in [#1105](https://github.com/jlowin/fastmcp/pull/1105)

  ### Fixes 🐞

  * Fix OpenAPI deepObject style parameter encoding by [@jlowin](https://github.com/jlowin) in [#1122](https://github.com/jlowin/fastmcp/pull/1122)
  * xfail when github token is not set ('' or None) by [@jlowin](https://github.com/jlowin) in [#1123](https://github.com/jlowin/fastmcp/pull/1123)
  * fix: replace oneOf with anyOf in OpenAPI output schemas by [@MagnusS0](https://github.com/MagnusS0) in [#1119](https://github.com/jlowin/fastmcp/pull/1119)
  * Fix middleware list result types by [@jlowin](https://github.com/jlowin) in [#1125](https://github.com/jlowin/fastmcp/pull/1125)
  * Improve console width for logo by [@jlowin](https://github.com/jlowin) in [#1126](https://github.com/jlowin/fastmcp/pull/1126)

  ### Docs 📚

  * Improve transport + integration docs by [@jlowin](https://github.com/jlowin) in [#1103](https://github.com/jlowin/fastmcp/pull/1103)
  * Update proxy.mdx by [@coldfire-x](https://github.com/coldfire-x) in [#1108](https://github.com/jlowin/fastmcp/pull/1108)

  ### Other Changes 🦾

  * Update github remote server tests with secret by [@jlowin](https://github.com/jlowin) in [#1112](https://github.com/jlowin/fastmcp/pull/1112)

  ## New Contributors

  * [@coldfire-x](https://github.com/coldfire-x) made their first contribution in [#1108](https://github.com/jlowin/fastmcp/pull/1108)
  * [@MagnusS0](https://github.com/MagnusS0) made their first contribution in [#1119](https://github.com/jlowin/fastmcp/pull/1119)

  **Full Changelog**: [v2.10.4...v2.10.5](https://github.com/jlowin/fastmcp/compare/v2.10.4...v2.10.5)
</Update>

<Update label="v2.10.4" description="2025-07-09">
  ## [v2.10.4: Transport-ation](https://github.com/jlowin/fastmcp/releases/tag/v2.10.4)

  A quick fix to ensure the CLI accepts "streamable-http" as a valid transport option.

  ## What's Changed

  ### Fixes 🐞

  * Ensure the CLI accepts "streamable-http" as a valid transport by [@jlowin](https://github.com/jlowin) in [#1099](https://github.com/jlowin/fastmcp/pull/1099)

  **Full Changelog**: [v2.10.3...v2.10.4](https://github.com/jlowin/fastmcp/compare/v2.10.3...v2.10.4)
</Update>

<Update label="v2.10.3" description="2025-07-09">
  ## [v2.10.3: CLI Me a River](https://github.com/jlowin/fastmcp/releases/tag/v2.10.3)

  A major CLI overhaul featuring a complete refactor from typer to cyclopts, new IDE integrations, and comprehensive OpenAPI improvements.

  ## What's Changed

  ### New Features 🎉

  * Refactor CLI from typer to cyclopts and add comprehensive tests by [@jlowin](https://github.com/jlowin) in [#1062](https://github.com/jlowin/fastmcp/pull/1062)
  * Add output schema support for OpenAPI tools by [@jlowin](https://github.com/jlowin) in [#1073](https://github.com/jlowin/fastmcp/pull/1073)

  ### Enhancements 🔧

  * Add Cursor support via CLI integration by [@jlowin](https://github.com/jlowin) in [#1052](https://github.com/jlowin/fastmcp/pull/1052)
  * Add Claude Code install integration by [@jlowin](https://github.com/jlowin) in [#1053](https://github.com/jlowin/fastmcp/pull/1053)
  * Generate MCP JSON config output from CLI as new `fastmcp install` command by [@jlowin](https://github.com/jlowin) in [#1056](https://github.com/jlowin/fastmcp/pull/1056)
  * Use isawaitable instead of iscoroutine by [@jlowin](https://github.com/jlowin) in [#1059](https://github.com/jlowin/fastmcp/pull/1059)
  * feat: Add `--path` Option to CLI for HTTP/SSE Route by [@davidbk-legit](https://github.com/davidbk-legit) in [#1087](https://github.com/jlowin/fastmcp/pull/1087)
  * Fix concurrent proxy client operations with session isolation by [@jlowin](https://github.com/jlowin) in [#1083](https://github.com/jlowin/fastmcp/pull/1083)

  ### Fixes 🐞

  * Refactor Client context management to avoid concurrency issue by [@hopeful0](https://github.com/hopeful0) in [#1054](https://github.com/jlowin/fastmcp/pull/1054)
  * Keep json schema \$defs on transform by [@strawgate](https://github.com/strawgate) in [#1066](https://github.com/jlowin/fastmcp/pull/1066)
  * Ensure fastmcp version copy is plaintext by [@jlowin](https://github.com/jlowin) in [#1071](https://github.com/jlowin/fastmcp/pull/1071)
  * Fix single-element list unwrapping in tool content by [@jlowin](https://github.com/jlowin) in [#1074](https://github.com/jlowin/fastmcp/pull/1074)
  * Fix max recursion error when pruning OpenAPI definitions by [@dimitribarbot](https://github.com/dimitribarbot) in [#1092](https://github.com/jlowin/fastmcp/pull/1092)
  * Fix OpenAPI tool name registration when modified by mcp\_component\_fn by [@jlowin](https://github.com/jlowin) in [#1096](https://github.com/jlowin/fastmcp/pull/1096)

  ### Docs 📚

  * Docs: add example of more concise way to use bearer auth by [@neilconway](https://github.com/neilconway) in [#1055](https://github.com/jlowin/fastmcp/pull/1055)
  * Update favicon by [@jlowin](https://github.com/jlowin) in [#1058](https://github.com/jlowin/fastmcp/pull/1058)
  * Update environment note by [@jlowin](https://github.com/jlowin) in [#1075](https://github.com/jlowin/fastmcp/pull/1075)
  * Add fastmcp version --copy documentation by [@jlowin](https://github.com/jlowin) in [#1076](https://github.com/jlowin/fastmcp/pull/1076)

  ### Other Changes 🦾

  * Remove asserts and add documentation following #1054 by [@jlowin](https://github.com/jlowin) in [#1057](https://github.com/jlowin/fastmcp/pull/1057)
  * Add --copy flag for fastmcp version by [@jlowin](https://github.com/jlowin) in [#1063](https://github.com/jlowin/fastmcp/pull/1063)
  * Fix docstring format for fastmcp.client.Client by [@neilconway](https://github.com/neilconway) in [#1094](https://github.com/jlowin/fastmcp/pull/1094)

  ## New Contributors

  * [@neilconway](https://github.com/neilconway) made their first contribution in [#1055](https://github.com/jlowin/fastmcp/pull/1055)
  * [@davidbk-legit](https://github.com/davidbk-legit) made their first contribution in [#1087](https://github.com/jlowin/fastmcp/pull/1087)
  * [@dimitribarbot](https://github.com/dimitribarbot) made their first contribution in [#1092](https://github.com/jlowin/fastmcp/pull/1092)

  **Full Changelog**: [v2.10.2...v2.10.3](https://github.com/jlowin/fastmcp/compare/v2.10.2...v2.10.3)
</Update>

<Update label="v2.10.2" description="2025-07-05">
  ## [v2.10.2: Forward March](https://github.com/jlowin/fastmcp/releases/tag/v2.10.2)

  The headline feature of this release is the ability to "forward" advanced MCP interactions like logging, progress, and elicitation through proxy servers. If the remote server requests an elicitation, the proxy client will pass that request to the new, "ultimate" client.

  ## What's Changed

  ### New Features 🎉

  * Proxy support advanced MCP features by [@hopeful0](https://github.com/hopeful0) in [#1022](https://github.com/jlowin/fastmcp/pull/1022)

  ### Enhancements 🔧

  * Re-add splash screen by [@jlowin](https://github.com/jlowin) in [#1027](https://github.com/jlowin/fastmcp/pull/1027)
  * Reduce banner padding by [@jlowin](https://github.com/jlowin) in [#1030](https://github.com/jlowin/fastmcp/pull/1030)
  * Allow per-server timeouts in MCPConfig by [@cegersdoerfer](https://github.com/cegersdoerfer) in [#1031](https://github.com/jlowin/fastmcp/pull/1031)
  * Support 'scp' claim for OAuth scopes in BearerAuthProvider by [@jlowin](https://github.com/jlowin) in [#1033](https://github.com/jlowin/fastmcp/pull/1033)
  * Add path expansion to image/audio/file by [@jlowin](https://github.com/jlowin) in [#1038](https://github.com/jlowin/fastmcp/pull/1038)
  * Ensure multi-client configurations use new ProxyClient by [@jlowin](https://github.com/jlowin) in [#1045](https://github.com/jlowin/fastmcp/pull/1045)

  ### Fixes 🐞

  * Expose stateless\_http kwarg for mcp.run() by [@jlowin](https://github.com/jlowin) in [#1018](https://github.com/jlowin/fastmcp/pull/1018)
  * Avoid propagating logs by [@jlowin](https://github.com/jlowin) in [#1042](https://github.com/jlowin/fastmcp/pull/1042)

  ### Docs 📚

  * Clean up docs by [@jlowin](https://github.com/jlowin) in [#1028](https://github.com/jlowin/fastmcp/pull/1028)
  * Docs: clarify server URL paths for ChatGPT integration by [@thap2331](https://github.com/thap2331) in [#1017](https://github.com/jlowin/fastmcp/pull/1017)

  ### Other Changes 🦾

  * Split giant openapi test file into smaller files by [@jlowin](https://github.com/jlowin) in [#1034](https://github.com/jlowin/fastmcp/pull/1034)
  * Add comprehensive OpenAPI 3.0 vs 3.1 compatibility tests by [@jlowin](https://github.com/jlowin) in [#1035](https://github.com/jlowin/fastmcp/pull/1035)
  * Update banner and use console.log by [@jlowin](https://github.com/jlowin) in [#1041](https://github.com/jlowin/fastmcp/pull/1041)

  ## New Contributors

  * [@cegersdoerfer](https://github.com/cegersdoerfer) made their first contribution in [#1031](https://github.com/jlowin/fastmcp/pull/1031)
  * [@hopeful0](https://github.com/hopeful0) made their first contribution in [#1022](https://github.com/jlowin/fastmcp/pull/1022)
  * [@thap2331](https://github.com/thap2331) made their first contribution in [#1017](https://github.com/jlowin/fastmcp/pull/1017)

  **Full Changelog**: [v2.10.1...v2.10.2](https://github.com/jlowin/fastmcp/compare/v2.10.1...v2.10.2)
</Update>

<Update label="v2.10.1" description="2025-07-02">
  ## [v2.10.1: Revert to Sender](https://github.com/jlowin/fastmcp/releases/tag/v2.10.1)

  A quick patch to revert the CLI banner that was added in v2.10.0.

  ## What's Changed

  ### Docs 📚

  * Update changelog.mdx by [@jlowin](https://github.com/jlowin) in [#1009](https://github.com/jlowin/fastmcp/pull/1009)
  * Revert "Add CLI banner" by [@jlowin](https://github.com/jlowin) in [#1011](https://github.com/jlowin/fastmcp/pull/1011)

  **Full Changelog**: [v2.10.0...v2.10.1](https://github.com/jlowin/fastmcp/compare/v2.10.0...v2.10.1)
</Update>

<Update label="v2.10.0" description="2024-07-01">
  ## [v2.10.0: Great Spec-tations](https://github.com/jlowin/fastmcp/releases/tag/v2.10.0)

  FastMCP 2.10 brings full compliance with the 6/18/2025 MCP spec update, introducing elicitation support for dynamic server-client communication and output schemas for structured tool responses. Please note that due to these changes, this release also includes a breaking change to the return signature of `client.call_tool()`.

  ### Elicitation Support

  Elicitation allows MCP servers to request additional information from clients during tool execution, enabling more interactive and dynamic server behavior. This opens up new possibilities for tools that need user input or confirmation during execution.

  ### Output Schemas

  Tools can now define structured output schemas, ensuring that responses conform to expected formats and making tool integration more predictable and type-safe.

  ## What's Changed

  ### New Features 🎉

  * MCP 6/18/25: Add output schema to tools by [@jlowin](https://github.com/jlowin) in [#901](https://github.com/jlowin/fastmcp/pull/901)
  * MCP 6/18/25: Elicitation support by [@jlowin](https://github.com/jlowin) in [#889](https://github.com/jlowin/fastmcp/pull/889)

  ### Enhancements 🔧

  * Update types + tests for SDK changes by [@jlowin](https://github.com/jlowin) in [#888](https://github.com/jlowin/fastmcp/pull/888)
  * MCP 6/18/25: Update auth primitives by [@jlowin](https://github.com/jlowin) in [#966](https://github.com/jlowin/fastmcp/pull/966)
  * Add OpenAPI extensions support to HTTPRoute by [@maddymanu](https://github.com/maddymanu) in [#977](https://github.com/jlowin/fastmcp/pull/977)
  * Add title field support to FastMCP components by [@jlowin](https://github.com/jlowin) in [#982](https://github.com/jlowin/fastmcp/pull/982)
  * Support implicit Elicitation acceptance by [@jlowin](https://github.com/jlowin) in [#983](https://github.com/jlowin/fastmcp/pull/983)
  * Support 'no response' elicitation requests by [@jlowin](https://github.com/jlowin) in [#992](https://github.com/jlowin/fastmcp/pull/992)
  * Add Support for Configurable Algorithms by [@sstene1](https://github.com/sstene1) in [#997](https://github.com/jlowin/fastmcp/pull/997)

  ### Fixes 🐞

  * Improve stdio error handling to raise connection failures immediately by [@jlowin](https://github.com/jlowin) in [#984](https://github.com/jlowin/fastmcp/pull/984)
  * Fix type hints for FunctionResource:fn by [@CfirTsabari](https://github.com/CfirTsabari) in [#986](https://github.com/jlowin/fastmcp/pull/986)
  * Update link to OpenAI MCP example by [@mossbanay](https://github.com/mossbanay) in [#985](https://github.com/jlowin/fastmcp/pull/985)
  * Fix output schema generation edge case by [@jlowin](https://github.com/jlowin) in [#995](https://github.com/jlowin/fastmcp/pull/995)
  * Refactor array parameter formatting to reduce code duplication by [@jlowin](https://github.com/jlowin) in [#1007](https://github.com/jlowin/fastmcp/pull/1007)
  * Fix OpenAPI array parameter explode handling by [@jlowin](https://github.com/jlowin) in [#1008](https://github.com/jlowin/fastmcp/pull/1008)

  ### Breaking Changes 🛫

  * MCP 6/18/25: Upgrade to mcp 1.10 by [@jlowin](https://github.com/jlowin) in [#887](https://github.com/jlowin/fastmcp/pull/887)

  ### Docs 📚

  * Update middleware imports and documentation by [@jlowin](https://github.com/jlowin) in [#999](https://github.com/jlowin/fastmcp/pull/999)
  * Update OpenAI docs by [@jlowin](https://github.com/jlowin) in [#1001](https://github.com/jlowin/fastmcp/pull/1001)
  * Add CLI banner by [@jlowin](https://github.com/jlowin) in [#1005](https://github.com/jlowin/fastmcp/pull/1005)

  ### Examples & Contrib 💡

  * Component Manager by [@gorocode](https://github.com/gorocode) in [#976](https://github.com/jlowin/fastmcp/pull/976)

  ### Other Changes 🦾

  * Minor auth improvements by [@jlowin](https://github.com/jlowin) in [#967](https://github.com/jlowin/fastmcp/pull/967)
  * Add .ccignore for copychat by [@jlowin](https://github.com/jlowin) in [#1000](https://github.com/jlowin/fastmcp/pull/1000)

  ## New Contributors

  * [@maddymanu](https://github.com/maddymanu) made their first contribution in [#977](https://github.com/jlowin/fastmcp/pull/977)
  * [@github0hello](https://github.com/github0hello) made their first contribution in [#979](https://github.com/jlowin/fastmcp/pull/979)
  * [@tommitt](https://github.com/tommitt) made their first contribution in [#975](https://github.com/jlowin/fastmcp/pull/975)
  * [@CfirTsabari](https://github.com/CfirTsabari) made their first contribution in [#986](https://github.com/jlowin/fastmcp/pull/986)
  * [@mossbanay](https://github.com/mossbanay) made their first contribution in [#985](https://github.com/jlowin/fastmcp/pull/985)
  * [@sstene1](https://github.com/sstene1) made their first contribution in [#997](https://github.com/jlowin/fastmcp/pull/997)

  **Full Changelog**: [v2.9.2...v2.10.0](https://github.com/jlowin/fastmcp/compare/v2.9.2...v2.10.0)
</Update>

<Update label="v2.9.2" description="2024-06-26">
  ## [v2.9.2: Safety Pin](https://github.com/jlowin/fastmcp/releases/tag/v2.9.2)

  This is a patch release to pin `mcp` below 1.10, which includes changes related to the 6/18/2025 MCP spec update and could potentially break functionality for some FastMCP users.

  ## What's Changed

  ### Docs 📚

  * Fix version badge for messages by [@jlowin](https://github.com/jlowin) in [#960](https://github.com/jlowin/fastmcp/pull/960)

  ### Dependencies 📦

  * Pin mcp dependency by [@jlowin](https://github.com/jlowin) in [#962](https://github.com/jlowin/fastmcp/pull/962)

  **Full Changelog**: [v2.9.1...v2.9.2](https://github.com/jlowin/fastmcp/compare/v2.9.1...v2.9.2)
</Update>

<Update label="v2.9.1" description="2024-06-26">
  ## [v2.9.1: Call Me Maybe](https://github.com/jlowin/fastmcp/releases/tag/v2.9.1)

  FastMCP 2.9.1 introduces automatic MCP list change notifications, allowing servers to notify clients when tools, resources, or prompts are dynamically updated. This enables more responsive and adaptive MCP integrations.

  ## What's Changed

  ### New Features 🎉

  * Add automatic MCP list change notifications and client message handling by [@jlowin](https://github.com/jlowin) in [#939](https://github.com/jlowin/fastmcp/pull/939)

  ### Enhancements 🔧

  * Add debug logging to bearer token authentication by [@jlowin](https://github.com/jlowin) in [#952](https://github.com/jlowin/fastmcp/pull/952)

  ### Fixes 🐞

  * Fix duplicate error logging in exception handlers by [@jlowin](https://github.com/jlowin) in [#938](https://github.com/jlowin/fastmcp/pull/938)
  * Fix parameter location enum handling in OpenAPI parser by [@jlowin](https://github.com/jlowin) in [#953](https://github.com/jlowin/fastmcp/pull/953)
  * Fix external schema reference handling in OpenAPI parser by [@jlowin](https://github.com/jlowin) in [#954](https://github.com/jlowin/fastmcp/pull/954)

  ### Docs 📚

  * Update changelog for 2.9 release by [@jlowin](https://github.com/jlowin) in [#929](https://github.com/jlowin/fastmcp/pull/929)
  * Regenerate API references by [@zzstoatzz](https://github.com/zzstoatzz) in [#935](https://github.com/jlowin/fastmcp/pull/935)
  * Regenerate API references by [@zzstoatzz](https://github.com/zzstoatzz) in [#947](https://github.com/jlowin/fastmcp/pull/947)
  * Regenerate API references by [@zzstoatzz](https://github.com/zzstoatzz) in [#949](https://github.com/jlowin/fastmcp/pull/949)

  ### Examples & Contrib 💡

  * Add `create_thread` tool to bsky MCP server by [@zzstoatzz](https://github.com/zzstoatzz) in [#927](https://github.com/jlowin/fastmcp/pull/927)
  * Update `mount_example.py` to work with current fastmcp API by [@rajephon](https://github.com/rajephon) in [#957](https://github.com/jlowin/fastmcp/pull/957)

  ## New Contributors

  * [@rajephon](https://github.com/rajephon) made their first contribution in [#957](https://github.com/jlowin/fastmcp/pull/957)

  **Full Changelog**: [v2.9.0...v2.9.1](https://github.com/jlowin/fastmcp/compare/v2.9.0...v2.9.1)
</Update>

<Update label="v2.9.0" description="2024-06-23">
  ## [v2.9.0: Stuck in the Middleware With You](https://github.com/jlowin/fastmcp/releases/tag/v2.9.0)

  FastMCP 2.9 introduces two important features that push beyond the basic MCP protocol: MCP Middleware and server-side type conversion.

  ### MCP Middleware

  MCP middleware lets you intercept and modify requests and responses at the protocol level, giving you powerful capabilities for logging, authentication, validation, and more. This is particularly useful for building production-ready MCP servers that need sophisticated request handling.

  ### Server-side Type Conversion

  This release also introduces server-side type conversion for prompt arguments, ensuring that data is properly formatted before being passed to your functions. This reduces the burden on individual tools and prompts to handle type validation and conversion.

  ## What's Changed

  ### New Features 🎉

  * Add File utility for binary data by [@gorocode](https://github.com/gorocode) in [#843](https://github.com/jlowin/fastmcp/pull/843)
  * Consolidate prefix logic into FastMCP methods by [@jlowin](https://github.com/jlowin) in [#861](https://github.com/jlowin/fastmcp/pull/861)
  * Add MCP Middleware by [@jlowin](https://github.com/jlowin) in [#870](https://github.com/jlowin/fastmcp/pull/870)
  * Implement server-side type conversion for prompt arguments by [@jlowin](https://github.com/jlowin) in [#908](https://github.com/jlowin/fastmcp/pull/908)

  ### Enhancements 🔧

  * Fix tool description indentation issue by [@zfflxx](https://github.com/zfflxx) in [#845](https://github.com/jlowin/fastmcp/pull/845)
  * Add version parameter to FastMCP constructor by [@mkyutani](https://github.com/mkyutani) in [#842](https://github.com/jlowin/fastmcp/pull/842)
  * Update version to not be positional by [@jlowin](https://github.com/jlowin) in [#848](https://github.com/jlowin/fastmcp/pull/848)
  * Add key to component by [@jlowin](https://github.com/jlowin) in [#869](https://github.com/jlowin/fastmcp/pull/869)
  * Add session\_id property to Context for data sharing by [@jlowin](https://github.com/jlowin) in [#881](https://github.com/jlowin/fastmcp/pull/881)
  * Fix CORS documentation example by [@jlowin](https://github.com/jlowin) in [#895](https://github.com/jlowin/fastmcp/pull/895)

  ### Fixes 🐞

  * "report\_progress missing passing related\_request\_id causes notifications not working" by [@alexsee](https://github.com/alexsee) in [#838](https://github.com/jlowin/fastmcp/pull/838)
  * Fix JWT issuer validation to support string values per RFC 7519 by [@jlowin](https://github.com/jlowin) in [#892](https://github.com/jlowin/fastmcp/pull/892)
  * Fix BearerAuthProvider audience type annotations by [@jlowin](https://github.com/jlowin) in [#894](https://github.com/jlowin/fastmcp/pull/894)

  ### Docs 📚

  * Add CLAUDE.md development guidelines by [@jlowin](https://github.com/jlowin) in [#880](https://github.com/jlowin/fastmcp/pull/880)
  * Update context docs for session\_id property by [@jlowin](https://github.com/jlowin) in [#882](https://github.com/jlowin/fastmcp/pull/882)
  * Add API reference by [@zzstoatzz](https://github.com/zzstoatzz) in [#893](https://github.com/jlowin/fastmcp/pull/893)
  * Fix API ref rendering by [@zzstoatzz](https://github.com/zzstoatzz) in [#900](https://github.com/jlowin/fastmcp/pull/900)
  * Simplify docs nav by [@jlowin](https://github.com/jlowin) in [#902](https://github.com/jlowin/fastmcp/pull/902)
  * Add fastmcp inspect command by [@jlowin](https://github.com/jlowin) in [#904](https://github.com/jlowin/fastmcp/pull/904)
  * Update client docs by [@jlowin](https://github.com/jlowin) in [#912](https://github.com/jlowin/fastmcp/pull/912)
  * Update docs nav by [@jlowin](https://github.com/jlowin) in [#913](https://github.com/jlowin/fastmcp/pull/913)
  * Update integration documentation for Claude Desktop, ChatGPT, and Claude Code by [@jlowin](https://github.com/jlowin) in [#915](https://github.com/jlowin/fastmcp/pull/915)
  * Add http as an alias for streamable http by [@jlowin](https://github.com/jlowin) in [#917](https://github.com/jlowin/fastmcp/pull/917)
  * Clean up parameter documentation by [@jlowin](https://github.com/jlowin) in [#918](https://github.com/jlowin/fastmcp/pull/918)
  * Add middleware examples for timing, logging, rate limiting, and error handling by [@jlowin](https://github.com/jlowin) in [#919](https://github.com/jlowin/fastmcp/pull/919)
  * ControlFlow → FastMCP rename by [@jlowin](https://github.com/jlowin) in [#922](https://github.com/jlowin/fastmcp/pull/922)

  ### Examples & Contrib 💡

  * Add contrib.mcp\_mixin support for annotations by [@rsp2k](https://github.com/rsp2k) in [#860](https://github.com/jlowin/fastmcp/pull/860)
  * Add ATProto (Bluesky) MCP Server Example by [@zzstoatzz](https://github.com/zzstoatzz) in [#916](https://github.com/jlowin/fastmcp/pull/916)
  * Fix path in atproto example pyproject by [@zzstoatzz](https://github.com/zzstoatzz) in [#920](https://github.com/jlowin/fastmcp/pull/920)
  * Remove uv source in example by [@zzstoatzz](https://github.com/zzstoatzz) in [#921](https://github.com/jlowin/fastmcp/pull/921)

  ## New Contributors

  * [@alexsee](https://github.com/alexsee) made their first contribution in [#838](https://github.com/jlowin/fastmcp/pull/838)
  * [@zfflxx](https://github.com/zfflxx) made their first contribution in [#845](https://github.com/jlowin/fastmcp/pull/845)
  * [@mkyutani](https://github.com/mkyutani) made their first contribution in [#842](https://github.com/jlowin/fastmcp/pull/842)
  * [@gorocode](https://github.com/gorocode) made their first contribution in [#843](https://github.com/jlowin/fastmcp/pull/843)
  * [@rsp2k](https://github.com/rsp2k) made their first contribution in [#860](https://github.com/jlowin/fastmcp/pull/860)
  * [@owtaylor](https://github.com/owtaylor) made their first contribution in [#897](https://github.com/jlowin/fastmcp/pull/897)
  * [@Jason-CKY](https://github.com/Jason-CKY) made their first contribution in [#906](https://github.com/jlowin/fastmcp/pull/906)

  **Full Changelog**: [v2.8.1...v2.9.0](https://github.com/jlowin/fastmcp/compare/v2.8.1...v2.9.0)
</Update>

<Update label="v2.8.1" description="2024-06-15">
  ## [v2.8.1: Sound Judgement](https://github.com/jlowin/fastmcp/releases/tag/v2.8.1)

  2.8.1 introduces audio support, as well as minor fixes and updates for deprecated features.

  ### Audio Support

  This release adds support for audio content in MCP tools and resources, expanding FastMCP's multimedia capabilities beyond text and images.

  ## What's Changed

  ### New Features 🎉

  * Add audio support by [@jlowin](https://github.com/jlowin) in [#833](https://github.com/jlowin/fastmcp/pull/833)

  ### Enhancements 🔧

  * Add flag for disabling deprecation warnings by [@jlowin](https://github.com/jlowin) in [#802](https://github.com/jlowin/fastmcp/pull/802)
  * Add examples to Tool Arg Param transformation by [@strawgate](https://github.com/strawgate) in [#806](https://github.com/jlowin/fastmcp/pull/806)

  ### Fixes 🐞

  * Restore .settings access as deprecated by [@jlowin](https://github.com/jlowin) in [#800](https://github.com/jlowin/fastmcp/pull/800)
  * Ensure handling of false http kwargs correctly; removed unused kwarg by [@jlowin](https://github.com/jlowin) in [#804](https://github.com/jlowin/fastmcp/pull/804)
  * Bump mcp 1.9.4 by [@jlowin](https://github.com/jlowin) in [#835](https://github.com/jlowin/fastmcp/pull/835)

  ### Docs 📚

  * Update changelog for 2.8.0 by [@jlowin](https://github.com/jlowin) in [#794](https://github.com/jlowin/fastmcp/pull/794)
  * Update welcome docs by [@jlowin](https://github.com/jlowin) in [#808](https://github.com/jlowin/fastmcp/pull/808)
  * Update headers in docs by [@jlowin](https://github.com/jlowin) in [#809](https://github.com/jlowin/fastmcp/pull/809)
  * Add MCP group to tutorials by [@jlowin](https://github.com/jlowin) in [#810](https://github.com/jlowin/fastmcp/pull/810)
  * Add Community section to documentation by [@zzstoatzz](https://github.com/zzstoatzz) in [#819](https://github.com/jlowin/fastmcp/pull/819)
  * Add 2.8 update by [@jlowin](https://github.com/jlowin) in [#821](https://github.com/jlowin/fastmcp/pull/821)
  * Embed YouTube videos in community showcase by [@zzstoatzz](https://github.com/zzstoatzz) in [#820](https://github.com/jlowin/fastmcp/pull/820)

  ### Other Changes 🦾

  * Ensure http args are passed through by [@jlowin](https://github.com/jlowin) in [#803](https://github.com/jlowin/fastmcp/pull/803)
  * Fix install link in readme by [@jlowin](https://github.com/jlowin) in [#836](https://github.com/jlowin/fastmcp/pull/836)

  **Full Changelog**: [v2.8.0...v2.8.1](https://github.com/jlowin/fastmcp/compare/v2.8.0...v2.8.1)
</Update>

<Update label="v2.8.0" description="2024-06-10">
  ## [v2.8.0: Transform and Roll Out](https://github.com/jlowin/fastmcp/releases/tag/v2.8.0)

  FastMCP 2.8.0 introduces powerful new ways to customize and control your MCP servers!

  ### Tool Transformation

  The highlight of this release is first-class [**Tool Transformation**](/patterns/tool-transformation), a new feature that lets you create enhanced variations of existing tools. You can now easily rename arguments, hide parameters, modify descriptions, and even wrap tools with custom validation or post-processing logic—all without rewriting the original code. This makes it easier than ever to adapt generic tools for specific LLM use cases or to simplify complex APIs. Huge thanks to [@strawgate](https://github.com/strawgate) for partnering on this, starting with [#591](https://github.com/jlowin/fastmcp/discussions/591) and [#599](https://github.com/jlowin/fastmcp/pull/599) and continuing offline.

  ### Component Control

  This release also gives you more granular control over which components are exposed to clients. With new [**tag-based filtering**](/servers/server#tag-based-filtering), you can selectively enable or disable tools, resources, and prompts based on tags, perfect for managing different environments or user permissions. Complementing this, every component now supports being [programmatically enabled or disabled](/servers/tools#disabling-tools), offering dynamic control over your server's capabilities.

  ### Tools-by-Default

  Finally, to improve compatibility with a wider range of LLM clients, this release changes the default behavior for OpenAPI integration: all API endpoints are now converted to `Tools` by default. This is a **breaking change** but pragmatically necessitated by the fact that the majority of MCP clients available today are, sadly, only compatible with MCP tools. Therefore, this change significantly simplifies the out-of-the-box experience and ensures your entire API is immediately accessible to any tool-using agent.

  ## What's Changed

  ### New Features 🎉

  * First-class tool transformation by [@jlowin](https://github.com/jlowin) in [#745](https://github.com/jlowin/fastmcp/pull/745)
  * Support enable/disable for all FastMCP components (tools, prompts, resources, templates) by [@jlowin](https://github.com/jlowin) in [#781](https://github.com/jlowin/fastmcp/pull/781)
  * Add support for tag-based component filtering by [@jlowin](https://github.com/jlowin) in [#748](https://github.com/jlowin/fastmcp/pull/748)
  * Allow tag assignments for OpenAPI by [@jlowin](https://github.com/jlowin) in [#791](https://github.com/jlowin/fastmcp/pull/791)

  ### Enhancements 🔧

  * Create common base class for components by [@jlowin](https://github.com/jlowin) in [#776](https://github.com/jlowin/fastmcp/pull/776)
  * Move components to own file; add resource by [@jlowin](https://github.com/jlowin) in [#777](https://github.com/jlowin/fastmcp/pull/777)
  * Update FastMCP component with **eq** and **repr** by [@jlowin](https://github.com/jlowin) in [#779](https://github.com/jlowin/fastmcp/pull/779)
  * Remove open-ended and server-specific settings by [@jlowin](https://github.com/jlowin) in [#750](https://github.com/jlowin/fastmcp/pull/750)

  ### Fixes 🐞

  * Ensure client is only initialized once by [@jlowin](https://github.com/jlowin) in [#758](https://github.com/jlowin/fastmcp/pull/758)
  * Fix field validator for resource by [@jlowin](https://github.com/jlowin) in [#778](https://github.com/jlowin/fastmcp/pull/778)
  * Ensure proxies can overwrite remote tools without falling back to the remote by [@jlowin](https://github.com/jlowin) in [#782](https://github.com/jlowin/fastmcp/pull/782)

  ### Breaking Changes 🛫

  * Treat all openapi routes as tools by [@jlowin](https://github.com/jlowin) in [#788](https://github.com/jlowin/fastmcp/pull/788)
  * Fix issue with global OpenAPI tags by [@jlowin](https://github.com/jlowin) in [#792](https://github.com/jlowin/fastmcp/pull/792)

  ### Docs 📚

  * Minor docs updates by [@jlowin](https://github.com/jlowin) in [#755](https://github.com/jlowin/fastmcp/pull/755)
  * Add 2.7 update by [@jlowin](https://github.com/jlowin) in [#756](https://github.com/jlowin/fastmcp/pull/756)
  * Reduce 2.7 image size by [@jlowin](https://github.com/jlowin) in [#757](https://github.com/jlowin/fastmcp/pull/757)
  * Update updates.mdx by [@jlowin](https://github.com/jlowin) in [#765](https://github.com/jlowin/fastmcp/pull/765)
  * Hide docs sidebar scrollbar by default by [@jlowin](https://github.com/jlowin) in [#766](https://github.com/jlowin/fastmcp/pull/766)
  * Add "stop vibe testing" to tutorials by [@jlowin](https://github.com/jlowin) in [#767](https://github.com/jlowin/fastmcp/pull/767)
  * Add docs links by [@jlowin](https://github.com/jlowin) in [#768](https://github.com/jlowin/fastmcp/pull/768)
  * Fix: updated variable name under Gemini remote client by [@yrangana](https://github.com/yrangana) in [#769](https://github.com/jlowin/fastmcp/pull/769)
  * Revert "Hide docs sidebar scrollbar by default" by [@jlowin](https://github.com/jlowin) in [#770](https://github.com/jlowin/fastmcp/pull/770)
  * Add updates by [@jlowin](https://github.com/jlowin) in [#773](https://github.com/jlowin/fastmcp/pull/773)
  * Add tutorials by [@jlowin](https://github.com/jlowin) in [#783](https://github.com/jlowin/fastmcp/pull/783)
  * Update LLM-friendly docs by [@jlowin](https://github.com/jlowin) in [#784](https://github.com/jlowin/fastmcp/pull/784)
  * Update oauth.mdx by [@JeremyCraigMartinez](https://github.com/JeremyCraigMartinez) in [#787](https://github.com/jlowin/fastmcp/pull/787)
  * Add changelog by [@jlowin](https://github.com/jlowin) in [#789](https://github.com/jlowin/fastmcp/pull/789)
  * Add tutorials by [@jlowin](https://github.com/jlowin) in [#790](https://github.com/jlowin/fastmcp/pull/790)
  * Add docs for tag-based filtering by [@jlowin](https://github.com/jlowin) in [#793](https://github.com/jlowin/fastmcp/pull/793)

  ### Other Changes 🦾

  * Create dependabot.yml by [@jlowin](https://github.com/jlowin) in [#759](https://github.com/jlowin/fastmcp/pull/759)
  * Bump astral-sh/setup-uv from 3 to 6 by [@dependabot](https://github.com/dependabot) in [#760](https://github.com/jlowin/fastmcp/pull/760)
  * Add dependencies section to release by [@jlowin](https://github.com/jlowin) in [#761](https://github.com/jlowin/fastmcp/pull/761)
  * Remove extra imports for MCPConfig by [@Maanas-Verma](https://github.com/Maanas-Verma) in [#763](https://github.com/jlowin/fastmcp/pull/763)
  * Split out enhancements in release notes by [@jlowin](https://github.com/jlowin) in [#764](https://github.com/jlowin/fastmcp/pull/764)

  ## New Contributors

  * [@dependabot](https://github.com/dependabot) made their first contribution in [#760](https://github.com/jlowin/fastmcp/pull/760)
  * [@Maanas-Verma](https://github.com/Maanas-Verma) made their first contribution in [#763](https://github.com/jlowin/fastmcp/pull/763)
  * [@JeremyCraigMartinez](https://github.com/JeremyCraigMartinez) made their first contribution in [#787](https://github.com/jlowin/fastmcp/pull/787)

  **Full Changelog**: [v2.7.1...v2.8.0](https://github.com/jlowin/fastmcp/compare/v2.7.1...v2.8.0)
</Update>

<Update label="v2.7.1" description="2024-06-08">
  ## [v2.7.1: The Bearer Necessities](https://github.com/jlowin/fastmcp/releases/tag/v2.7.1)

  This release primarily contains a fix for parsing string tokens that are provided to FastMCP clients.

  ### New Features 🎉

  * Respect cache setting, set default to 1 second by [@jlowin](https://github.com/jlowin) in [#747](https://github.com/jlowin/fastmcp/pull/747)

  ### Fixes 🐞

  * Ensure event store is properly typed by [@jlowin](https://github.com/jlowin) in [#753](https://github.com/jlowin/fastmcp/pull/753)
  * Fix passing token string to client auth & add auth to MCPConfig clients by [@jlowin](https://github.com/jlowin) in [#754](https://github.com/jlowin/fastmcp/pull/754)

  ### Docs 📚

  * Docs : fix client to mcp\_client in Gemini example by [@yrangana](https://github.com/yrangana) in [#734](https://github.com/jlowin/fastmcp/pull/734)
  * update add tool docstring by [@strawgate](https://github.com/strawgate) in [#739](https://github.com/jlowin/fastmcp/pull/739)
  * Fix contrib link by [@richardkmichael](https://github.com/richardkmichael) in [#749](https://github.com/jlowin/fastmcp/pull/749)

  ### Other Changes 🦾

  * Switch Pydantic defaults to kwargs by [@strawgate](https://github.com/strawgate) in [#731](https://github.com/jlowin/fastmcp/pull/731)
  * Fix Typo in CLI module by [@wfclark5](https://github.com/wfclark5) in [#737](https://github.com/jlowin/fastmcp/pull/737)
  * chore: fix prompt docstring by [@danb27](https://github.com/danb27) in [#752](https://github.com/jlowin/fastmcp/pull/752)
  * Add accept to excluded headers by [@jlowin](https://github.com/jlowin) in [#751](https://github.com/jlowin/fastmcp/pull/751)

  ### New Contributors

  * [@wfclark5](https://github.com/wfclark5) made their first contribution in [#737](https://github.com/jlowin/fastmcp/pull/737)
  * [@richardkmichael](https://github.com/richardkmichael) made their first contribution in [#749](https://github.com/jlowin/fastmcp/pull/749)
  * [@danb27](https://github.com/danb27) made their first contribution in [#752](https://github.com/jlowin/fastmcp/pull/752)

  **Full Changelog**: [v2.7.0...v2.7.1](https://github.com/jlowin/fastmcp/compare/v2.7.0...v2.7.1)
</Update>

<Update label="v2.7.0" description="2024-06-05">
  ## [v2.7.0: Pare Programming](https://github.com/jlowin/fastmcp/releases/tag/v2.7.0)

  This is primarily a housekeeping release to remove or deprecate cruft that's accumulated since v1. Primarily, this release refactors FastMCP's internals in preparation for features planned in the next few major releases. However please note that as a result, this release has some minor breaking changes (which is why it's 2.7, not 2.6.2, in accordance with repo guidelines) though not to the core user-facing APIs.

  ### Breaking Changes 🛫

  * decorators return the objects they create, not the decorated function
  * websockets is an optional dependency
  * methods on the server for automatically converting functions into tools/resources/prompts have been deprecated in favor of using the decorators directly

  ### New Features 🎉

  * allow passing flags to servers by [@zzstoatzz](https://github.com/zzstoatzz) in [#690](https://github.com/jlowin/fastmcp/pull/690)
  * replace $ref pointing to `#/components/schemas/` with `#/$defs/\` by [@phateffect](https://github.com/phateffect) in [#697](https://github.com/jlowin/fastmcp/pull/697)
  * Split Tool into Tool and FunctionTool by [@jlowin](https://github.com/jlowin) in [#700](https://github.com/jlowin/fastmcp/pull/700)
  * Use strict basemodel for Prompt; relax from\_function deprecation by [@jlowin](https://github.com/jlowin) in [#701](https://github.com/jlowin/fastmcp/pull/701)
  * Formalize resource/functionresource replationship by [@jlowin](https://github.com/jlowin) in [#702](https://github.com/jlowin/fastmcp/pull/702)
  * Formalize template/functiontemplate split by [@jlowin](https://github.com/jlowin) in [#703](https://github.com/jlowin/fastmcp/pull/703)
  * Support flexible @tool decorator call patterns by [@jlowin](https://github.com/jlowin) in [#706](https://github.com/jlowin/fastmcp/pull/706)
  * Ensure deprecation warnings have stacklevel=2 by [@jlowin](https://github.com/jlowin) in [#710](https://github.com/jlowin/fastmcp/pull/710)
  * Allow naked prompt decorator by [@jlowin](https://github.com/jlowin) in [#711](https://github.com/jlowin/fastmcp/pull/711)

  ### Fixes 🐞

  * Updates / Fixes for Tool Content Conversion by [@strawgate](https://github.com/strawgate) in [#642](https://github.com/jlowin/fastmcp/pull/642)
  * Fix pr labeler permissions by [@jlowin](https://github.com/jlowin) in [#708](https://github.com/jlowin/fastmcp/pull/708)
  * remove -n auto by [@jlowin](https://github.com/jlowin) in [#709](https://github.com/jlowin/fastmcp/pull/709)
  * Fix links in README.md by [@alainivars](https://github.com/alainivars) in [#723](https://github.com/jlowin/fastmcp/pull/723)

  Happily, this release DOES permit the use of "naked" decorators to align with Pythonic practice:

  ```python
  @mcp.tool
  def my_tool():
      ...
  ```

  **Full Changelog**: [v2.6.2...v2.7.0](https://github.com/jlowin/fastmcp/compare/v2.6.2...v2.7.0)
</Update>

<Update label="v2.6.1" description="2024-06-03">
  ## [v2.6.1: Blast Auth (second ignition)](https://github.com/jlowin/fastmcp/releases/tag/v2.6.1)

  This is a patch release to restore py.typed in #686.

  ### Docs 📚

  * Update readme by [@jlowin](https://github.com/jlowin) in [#679](https://github.com/jlowin/fastmcp/pull/679)
  * Add gemini tutorial by [@jlowin](https://github.com/jlowin) in [#680](https://github.com/jlowin/fastmcp/pull/680)
  * Fix : fix path error to CLI Documentation by [@yrangana](https://github.com/yrangana) in [#684](https://github.com/jlowin/fastmcp/pull/684)
  * Update auth docs by [@jlowin](https://github.com/jlowin) in [#687](https://github.com/jlowin/fastmcp/pull/687)

  ### Other Changes 🦾

  * Remove deprecation notice by [@jlowin](https://github.com/jlowin) in [#677](https://github.com/jlowin/fastmcp/pull/677)
  * Delete server.py by [@jlowin](https://github.com/jlowin) in [#681](https://github.com/jlowin/fastmcp/pull/681)
  * Restore py.typed by [@jlowin](https://github.com/jlowin) in [#686](https://github.com/jlowin/fastmcp/pull/686)

  ### New Contributors

  * [@yrangana](https://github.com/yrangana) made their first contribution in [#684](https://github.com/jlowin/fastmcp/pull/684)

  **Full Changelog**: [v2.6.0...v2.6.1](https://github.com/jlowin/fastmcp/compare/v2.6.0...v2.6.1)
</Update>

<Update label="v2.6.0" description="2024-06-02">
  ## [v2.6.0: Blast Auth](https://github.com/jlowin/fastmcp/releases/tag/v2.6.0)

  ### New Features 🎉

  * Introduce MCP client oauth flow by [@jlowin](https://github.com/jlowin) in [#478](https://github.com/jlowin/fastmcp/pull/478)
  * Support providing tools at init by [@jlowin](https://github.com/jlowin) in [#647](https://github.com/jlowin/fastmcp/pull/647)
  * Simplify code for running servers in processes during tests by [@jlowin](https://github.com/jlowin) in [#649](https://github.com/jlowin/fastmcp/pull/649)
  * Add basic bearer auth for server and client by [@jlowin](https://github.com/jlowin) in [#650](https://github.com/jlowin/fastmcp/pull/650)
  * Support configuring bearer auth from env vars by [@jlowin](https://github.com/jlowin) in [#652](https://github.com/jlowin/fastmcp/pull/652)
  * feat(tool): add support for excluding arguments from tool definition by [@deepak-stratforge](https://github.com/deepak-stratforge) in [#626](https://github.com/jlowin/fastmcp/pull/626)
  * Add docs for server + client auth by [@jlowin](https://github.com/jlowin) in [#655](https://github.com/jlowin/fastmcp/pull/655)

  ### Fixes 🐞

  * fix: Support concurrency in FastMcpProxy (and Client) by [@Sillocan](https://github.com/Sillocan) in [#635](https://github.com/jlowin/fastmcp/pull/635)
  * Ensure Client.close() cleans up client context appropriately by [@jlowin](https://github.com/jlowin) in [#643](https://github.com/jlowin/fastmcp/pull/643)
  * Update client.mdx: ClientError namespace by [@mjkaye](https://github.com/mjkaye) in [#657](https://github.com/jlowin/fastmcp/pull/657)

  ### Docs 📚

  * Make FastMCPTransport support simulated Streamable HTTP Transport (didn't work) by [@jlowin](https://github.com/jlowin) in [#645](https://github.com/jlowin/fastmcp/pull/645)
  * Document exclude\_args by [@jlowin](https://github.com/jlowin) in [#653](https://github.com/jlowin/fastmcp/pull/653)
  * Update welcome by [@jlowin](https://github.com/jlowin) in [#673](https://github.com/jlowin/fastmcp/pull/673)
  * Add Anthropic + Claude desktop integration guides by [@jlowin](https://github.com/jlowin) in [#674](https://github.com/jlowin/fastmcp/pull/674)
  * Minor docs design updates by [@jlowin](https://github.com/jlowin) in [#676](https://github.com/jlowin/fastmcp/pull/676)

  ### Other Changes 🦾

  * Update test typing by [@jlowin](https://github.com/jlowin) in [#646](https://github.com/jlowin/fastmcp/pull/646)
  * Add OpenAI integration docs by [@jlowin](https://github.com/jlowin) in [#660](https://github.com/jlowin/fastmcp/pull/660)

  ### New Contributors

  * [@Sillocan](https://github.com/Sillocan) made their first contribution in [#635](https://github.com/jlowin/fastmcp/pull/635)
  * [@deepak-stratforge](https://github.com/deepak-stratforge) made their first contribution in [#626](https://github.com/jlowin/fastmcp/pull/626)
  * [@mjkaye](https://github.com/mjkaye) made their first contribution in [#657](https://github.com/jlowin/fastmcp/pull/657)

  **Full Changelog**: [v2.5.2...v2.6.0](https://github.com/jlowin/fastmcp/compare/v2.5.2...v2.6.0)
</Update>

<Update label="v2.5.2" description="2024-05-29">
  ## [v2.5.2: Stayin' Alive](https://github.com/jlowin/fastmcp/releases/tag/v2.5.2)

  ### New Features 🎉

  * Add graceful error handling for unreachable mounted servers by [@davenpi](https://github.com/davenpi) in [#605](https://github.com/jlowin/fastmcp/pull/605)
  * Improve type inference from client transport by [@jlowin](https://github.com/jlowin) in [#623](https://github.com/jlowin/fastmcp/pull/623)
  * Add keep\_alive param to reuse subprocess by [@jlowin](https://github.com/jlowin) in [#624](https://github.com/jlowin/fastmcp/pull/624)

  ### Fixes 🐞

  * Fix handling tools without descriptions by [@jlowin](https://github.com/jlowin) in [#610](https://github.com/jlowin/fastmcp/pull/610)
  * Don't print env vars to console when format is wrong by [@jlowin](https://github.com/jlowin) in [#615](https://github.com/jlowin/fastmcp/pull/615)
  * Ensure behavior-affecting headers are excluded when forwarding proxies/openapi by [@jlowin](https://github.com/jlowin) in [#620](https://github.com/jlowin/fastmcp/pull/620)

  ### Docs 📚

  * Add notes about uv and claude desktop by [@jlowin](https://github.com/jlowin) in [#597](https://github.com/jlowin/fastmcp/pull/597)

  ### Other Changes 🦾

  * add init\_timeout for mcp client by [@jfouret](https://github.com/jfouret) in [#607](https://github.com/jlowin/fastmcp/pull/607)
  * Add init\_timeout for mcp client (incl settings) by [@jlowin](https://github.com/jlowin) in [#609](https://github.com/jlowin/fastmcp/pull/609)
  * Support for uppercase letters at the log level by [@ksawaray](https://github.com/ksawaray) in [#625](https://github.com/jlowin/fastmcp/pull/625)

  ### New Contributors

  * [@jfouret](https://github.com/jfouret) made their first contribution in [#607](https://github.com/jlowin/fastmcp/pull/607)
  * [@ksawaray](https://github.com/ksawaray) made their first contribution in [#625](https://github.com/jlowin/fastmcp/pull/625)

  **Full Changelog**: [v2.5.1...v2.5.2](https://github.com/jlowin/fastmcp/compare/v2.5.1...v2.5.2)
</Update>

<Update label="v2.5.1" description="2024-05-24">
  ## [v2.5.1: Route Awakening (Part 2)](https://github.com/jlowin/fastmcp/releases/tag/v2.5.1)

  ### Fixes 🐞

  * Ensure content-length is always stripped from client headers by [@jlowin](https://github.com/jlowin) in [#589](https://github.com/jlowin/fastmcp/pull/589)

  ### Docs 📚

  * Fix redundant section of docs by [@jlowin](https://github.com/jlowin) in [#583](https://github.com/jlowin/fastmcp/pull/583)

  **Full Changelog**: [v2.5.0...v2.5.1](https://github.com/jlowin/fastmcp/compare/v2.5.0...v2.5.1)
</Update>

<Update label="v2.5.0" description="2024-05-24">
  ## [v2.5.0: Route Awakening](https://github.com/jlowin/fastmcp/releases/tag/v2.5.0)

  This release introduces completely new tools for generating and customizing MCP servers from OpenAPI specs and FastAPI apps, including popular requests like mechanisms for determining what routes map to what MCP components; renaming routes; and customizing the generated MCP components.

  ### New Features 🎉

  * Add FastMCP 1.0 server support for in-memory Client / Testing by [@jlowin](https://github.com/jlowin) in [#539](https://github.com/jlowin/fastmcp/pull/539)
  * Minor addition: add transport to stdio server in mcpconfig, with default by [@jlowin](https://github.com/jlowin) in [#555](https://github.com/jlowin/fastmcp/pull/555)
  * Raise an error if a Client is created with no servers in config by [@jlowin](https://github.com/jlowin) in [#554](https://github.com/jlowin/fastmcp/pull/554)
  * Expose model preferences in `Context.sample` for flexible model selection. by [@davenpi](https://github.com/davenpi) in [#542](https://github.com/jlowin/fastmcp/pull/542)
  * Ensure custom routes are respected by [@jlowin](https://github.com/jlowin) in [#558](https://github.com/jlowin/fastmcp/pull/558)
  * Add client method to send cancellation notifications by [@davenpi](https://github.com/davenpi) in [#563](https://github.com/jlowin/fastmcp/pull/563)
  * Enhance route map logic for include/exclude OpenAPI routes by [@jlowin](https://github.com/jlowin) in [#564](https://github.com/jlowin/fastmcp/pull/564)
  * Add tag-based route maps by [@jlowin](https://github.com/jlowin) in [#565](https://github.com/jlowin/fastmcp/pull/565)
  * Add advanced control of openAPI route creation by [@jlowin](https://github.com/jlowin) in [#566](https://github.com/jlowin/fastmcp/pull/566)
  * Make error masking configurable by [@jlowin](https://github.com/jlowin) in [#550](https://github.com/jlowin/fastmcp/pull/550)
  * Ensure client headers are passed through to remote servers by [@jlowin](https://github.com/jlowin) in [#575](https://github.com/jlowin/fastmcp/pull/575)
  * Use lowercase name for headers when comparing by [@jlowin](https://github.com/jlowin) in [#576](https://github.com/jlowin/fastmcp/pull/576)
  * Permit more flexible name generation for OpenAPI servers by [@jlowin](https://github.com/jlowin) in [#578](https://github.com/jlowin/fastmcp/pull/578)
  * Ensure that tools/templates/prompts are compatible with callable objects by [@jlowin](https://github.com/jlowin) in [#579](https://github.com/jlowin/fastmcp/pull/579)

  ### Docs 📚

  * Add version badge for prefix formats by [@jlowin](https://github.com/jlowin) in [#537](https://github.com/jlowin/fastmcp/pull/537)
  * Add versioning note to docs by [@jlowin](https://github.com/jlowin) in [#551](https://github.com/jlowin/fastmcp/pull/551)
  * Bump 2.3.6 references to 2.4.0 by [@jlowin](https://github.com/jlowin) in [#567](https://github.com/jlowin/fastmcp/pull/567)

  **Full Changelog**: [v2.4.0...v2.5.0](https://github.com/jlowin/fastmcp/compare/v2.4.0...v2.5.0)
</Update>

<Update label="v2.4.0" description="2024-05-21">
  ## [v2.4.0: Config and Conquer](https://github.com/jlowin/fastmcp/releases/tag/v2.4.0)

  **Note**: this release includes a backwards-incompatible change to how resources are prefixed when mounted in composed servers. However, it is only backwards-incompatible if users were running tests or manually loading resources by prefixed key; LLMs should not have any issue discovering the new route. See [Resource Prefix Formats](https://gofastmcp.com/servers/composition#resource-prefix-formats) for more.

  ### New Features 🎉

  * Allow \* Methods and all routes as tools shortcuts by [@jlowin](https://github.com/jlowin) in [#520](https://github.com/jlowin/fastmcp/pull/520)
  * Improved support for config dicts by [@jlowin](https://github.com/jlowin) in [#522](https://github.com/jlowin/fastmcp/pull/522)
  * Support creating clients from MCP config dicts, including multi-server clients by [@jlowin](https://github.com/jlowin) in [#527](https://github.com/jlowin/fastmcp/pull/527)
  * Make resource prefix format configurable by [@jlowin](https://github.com/jlowin) in [#534](https://github.com/jlowin/fastmcp/pull/534)

  ### Fixes 🐞

  * Avoid hanging on initializing server session by [@jlowin](https://github.com/jlowin) in [#523](https://github.com/jlowin/fastmcp/pull/523)

  ### Breaking Changes 🛫

  * Remove customizable separators; improve resource separator by [@jlowin](https://github.com/jlowin) in [#526](https://github.com/jlowin/fastmcp/pull/526)

  ### Docs 📚

  * Improve client documentation by [@jlowin](https://github.com/jlowin) in [#517](https://github.com/jlowin/fastmcp/pull/517)

  ### Other Changes 🦾

  * Ensure openapi path params are handled properly by [@jlowin](https://github.com/jlowin) in [#519](https://github.com/jlowin/fastmcp/pull/519)
  * better error when missing lifespan by [@zzstoatzz](https://github.com/zzstoatzz) in [#521](https://github.com/jlowin/fastmcp/pull/521)

  **Full Changelog**: [v2.3.5...v2.4.0](https://github.com/jlowin/fastmcp/compare/v2.3.5...v2.4.0)
</Update>

<Update label="v2.3.5" description="2024-05-20">
  ## [v2.3.5: Making Progress](https://github.com/jlowin/fastmcp/releases/tag/v2.3.5)

  ### New Features 🎉

  * support messages in progress notifications by [@rickygenhealth](https://github.com/rickygenhealth) in [#471](https://github.com/jlowin/fastmcp/pull/471)
  * feat: Add middleware option in server.run by [@Maxi91f](https://github.com/Maxi91f) in [#475](https://github.com/jlowin/fastmcp/pull/475)
  * Add lifespan property to app by [@jlowin](https://github.com/jlowin) in [#483](https://github.com/jlowin/fastmcp/pull/483)
  * Update `fastmcp run` to work with remote servers by [@jlowin](https://github.com/jlowin) in [#491](https://github.com/jlowin/fastmcp/pull/491)
  * Add FastMCP.as\_proxy() by [@jlowin](https://github.com/jlowin) in [#490](https://github.com/jlowin/fastmcp/pull/490)
  * Infer sse transport from urls containing /sse by [@jlowin](https://github.com/jlowin) in [#512](https://github.com/jlowin/fastmcp/pull/512)
  * Add progress handler to client by [@jlowin](https://github.com/jlowin) in [#513](https://github.com/jlowin/fastmcp/pull/513)
  * Store the initialize result on the client by [@jlowin](https://github.com/jlowin) in [#509](https://github.com/jlowin/fastmcp/pull/509)

  ### Fixes 🐞

  * Remove patch and use upstream SSEServerTransport by [@jlowin](https://github.com/jlowin) in [#425](https://github.com/jlowin/fastmcp/pull/425)

  ### Docs 📚

  * Update transport docs by [@jlowin](https://github.com/jlowin) in [#458](https://github.com/jlowin/fastmcp/pull/458)
  * update proxy docs + example by [@zzstoatzz](https://github.com/zzstoatzz) in [#460](https://github.com/jlowin/fastmcp/pull/460)
  * doc(asgi): Change custom route example to PlainTextResponse by [@mcw0933](https://github.com/mcw0933) in [#477](https://github.com/jlowin/fastmcp/pull/477)
  * Store FastMCP instance on app.state.fastmcp\_server by [@jlowin](https://github.com/jlowin) in [#489](https://github.com/jlowin/fastmcp/pull/489)
  * Improve AGENTS.md overview by [@jlowin](https://github.com/jlowin) in [#492](https://github.com/jlowin/fastmcp/pull/492)
  * Update release numbers for anticipated version by [@jlowin](https://github.com/jlowin) in [#516](https://github.com/jlowin/fastmcp/pull/516)

  ### Other Changes 🦾

  * run tests on all PRs by [@jlowin](https://github.com/jlowin) in [#468](https://github.com/jlowin/fastmcp/pull/468)
  * add null check by [@zzstoatzz](https://github.com/zzstoatzz) in [#473](https://github.com/jlowin/fastmcp/pull/473)
  * strict typing for `server.py` by [@zzstoatzz](https://github.com/zzstoatzz) in [#476](https://github.com/jlowin/fastmcp/pull/476)
  * Doc(quickstart): Fix import statements by [@mai-nakagawa](https://github.com/mai-nakagawa) in [#479](https://github.com/jlowin/fastmcp/pull/479)
  * Add labeler by [@jlowin](https://github.com/jlowin) in [#484](https://github.com/jlowin/fastmcp/pull/484)
  * Fix flaky timeout test by increasing timeout (#474) by [@davenpi](https://github.com/davenpi) in [#486](https://github.com/jlowin/fastmcp/pull/486)
  * Skipping `test_permission_error` if runner is root. by [@ZiadAmerr](https://github.com/ZiadAmerr) in [#502](https://github.com/jlowin/fastmcp/pull/502)
  * allow passing full uvicorn config by [@zzstoatzz](https://github.com/zzstoatzz) in [#504](https://github.com/jlowin/fastmcp/pull/504)
  * Skip timeout tests on windows by [@jlowin](https://github.com/jlowin) in [#514](https://github.com/jlowin/fastmcp/pull/514)

  ### New Contributors

  * [@rickygenhealth](https://github.com/rickygenhealth) made their first contribution in [#471](https://github.com/jlowin/fastmcp/pull/471)
  * [@Maxi91f](https://github.com/Maxi91f) made their first contribution in [#475](https://github.com/jlowin/fastmcp/pull/475)
  * [@mcw0933](https://github.com/mcw0933) made their first contribution in [#477](https://github.com/jlowin/fastmcp/pull/477)
  * [@mai-nakagawa](https://github.com/mai-nakagawa) made their first contribution in [#479](https://github.com/jlowin/fastmcp/pull/479)
  * [@ZiadAmerr](https://github.com/ZiadAmerr) made their first contribution in [#502](https://github.com/jlowin/fastmcp/pull/502)

  **Full Changelog**: [v2.3.4...v2.3.5](https://github.com/jlowin/fastmcp/compare/v2.3.4...v2.3.5)
</Update>

<Update label="v2.3.4" description="2024-05-15">
  ## [v2.3.4: Error Today, Gone Tomorrow](https://github.com/jlowin/fastmcp/releases/tag/v2.3.4)

  ### New Features 🎉

  * logging stack trace for easier debugging by [@jbkoh](https://github.com/jbkoh) in [#413](https://github.com/jlowin/fastmcp/pull/413)
  * add missing StreamableHttpTransport in client exports by [@yihuang](https://github.com/yihuang) in [#408](https://github.com/jlowin/fastmcp/pull/408)
  * Improve error handling for tools and resources by [@jlowin](https://github.com/jlowin) in [#434](https://github.com/jlowin/fastmcp/pull/434)
  * feat: add support for removing tools from server by [@davenpi](https://github.com/davenpi) in [#437](https://github.com/jlowin/fastmcp/pull/437)
  * Prune titles from JSONSchemas by [@jlowin](https://github.com/jlowin) in [#449](https://github.com/jlowin/fastmcp/pull/449)
  * Declare toolsChanged capability for stdio server. by [@davenpi](https://github.com/davenpi) in [#450](https://github.com/jlowin/fastmcp/pull/450)
  * Improve handling of exceptiongroups when raised in clients by [@jlowin](https://github.com/jlowin) in [#452](https://github.com/jlowin/fastmcp/pull/452)
  * Add timeout support to client by [@jlowin](https://github.com/jlowin) in [#455](https://github.com/jlowin/fastmcp/pull/455)

  ### Fixes 🐞

  * Pin to mcp 1.8.1 to resolve callback deadlocks with SHTTP by [@jlowin](https://github.com/jlowin) in [#427](https://github.com/jlowin/fastmcp/pull/427)
  * Add reprs for OpenAPI objects by [@jlowin](https://github.com/jlowin) in [#447](https://github.com/jlowin/fastmcp/pull/447)
  * Ensure openapi defs for structured objects are loaded properly by [@jlowin](https://github.com/jlowin) in [#448](https://github.com/jlowin/fastmcp/pull/448)
  * Ensure tests run against correct python version by [@jlowin](https://github.com/jlowin) in [#454](https://github.com/jlowin/fastmcp/pull/454)
  * Ensure result is only returned if a new key was found by [@jlowin](https://github.com/jlowin) in [#456](https://github.com/jlowin/fastmcp/pull/456)

  ### Docs 📚

  * Add documentation for tool removal by [@jlowin](https://github.com/jlowin) in [#440](https://github.com/jlowin/fastmcp/pull/440)

  ### Other Changes 🦾

  * Deprecate passing settings to the FastMCP instance by [@jlowin](https://github.com/jlowin) in [#424](https://github.com/jlowin/fastmcp/pull/424)
  * Add path prefix to test by [@jlowin](https://github.com/jlowin) in [#432](https://github.com/jlowin/fastmcp/pull/432)

  ### New Contributors

  * [@jbkoh](https://github.com/jbkoh) made their first contribution in [#413](https://github.com/jlowin/fastmcp/pull/413)
  * [@davenpi](https://github.com/davenpi) made their first contribution in [#437](https://github.com/jlowin/fastmcp/pull/437)

  **Full Changelog**: [v2.3.3...v2.3.4](https://github.com/jlowin/fastmcp/compare/v2.3.3...v2.3.4)
</Update>

<Update label="v2.3.3" description="2024-05-10">
  ## [v2.3.3: SSE you later](https://github.com/jlowin/fastmcp/releases/tag/v2.3.3)

  This is a hotfix for a bug introduced in 2.3.2 that broke SSE servers

  ### Fixes 🐞

  * Fix bug that sets message path and sse path to same value by [@jlowin](https://github.com/jlowin) in [#405](https://github.com/jlowin/fastmcp/pull/405)

  ### Docs 📚

  * Update composition docs by [@jlowin](https://github.com/jlowin) in [#403](https://github.com/jlowin/fastmcp/pull/403)

  ### Other Changes 🦾

  * Add test for no prefix when importing by [@jlowin](https://github.com/jlowin) in [#404](https://github.com/jlowin/fastmcp/pull/404)

  **Full Changelog**: [v2.3.2...v2.3.3](https://github.com/jlowin/fastmcp/compare/v2.3.2...v2.3.3)
</Update>

<Update label="v2.3.2" description="2024-05-10">
  ## [v2.3.2: Stuck in the Middleware With You](https://github.com/jlowin/fastmcp/releases/tag/v2.3.2)

  ### New Features 🎉

  * Allow users to pass middleware to starlette app constructors by [@jlowin](https://github.com/jlowin) in [#398](https://github.com/jlowin/fastmcp/pull/398)
  * Deprecate transport-specific methods on FastMCP server by [@jlowin](https://github.com/jlowin) in [#401](https://github.com/jlowin/fastmcp/pull/401)

  ### Docs 📚

  * Update CLI docs by [@jlowin](https://github.com/jlowin) in [#402](https://github.com/jlowin/fastmcp/pull/402)

  ### Other Changes 🦾

  * Adding 23 tests for CLI by [@didier-durand](https://github.com/didier-durand) in [#394](https://github.com/jlowin/fastmcp/pull/394)

  **Full Changelog**: [v2.3.1...v2.3.2](https://github.com/jlowin/fastmcp/compare/v2.3.1...v2.3.2)
</Update>

<Update label="v2.3.1" description="2024-05-09">
  ## [v2.3.1: For Good-nests Sake](https://github.com/jlowin/fastmcp/releases/tag/v2.3.1)

  This release primarily patches a long-standing bug with nested ASGI SSE servers.

  ### Fixes 🐞

  * Fix tool result serialization when the tool returns a list by [@strawgate](https://github.com/strawgate) in [#379](https://github.com/jlowin/fastmcp/pull/379)
  * Ensure FastMCP handles nested SSE and SHTTP apps properly in ASGI frameworks by [@jlowin](https://github.com/jlowin) in [#390](https://github.com/jlowin/fastmcp/pull/390)

  ### Docs 📚

  * Update transport docs by [@jlowin](https://github.com/jlowin) in [#377](https://github.com/jlowin/fastmcp/pull/377)
  * Add llms.txt to docs by [@jlowin](https://github.com/jlowin) in [#384](https://github.com/jlowin/fastmcp/pull/384)
  * Fixing various text typos by [@didier-durand](https://github.com/didier-durand) in [#385](https://github.com/jlowin/fastmcp/pull/385)

  ### Other Changes 🦾

  * Adding a few tests to Image type by [@didier-durand](https://github.com/didier-durand) in [#387](https://github.com/jlowin/fastmcp/pull/387)
  * Adding tests for TimedCache by [@didier-durand](https://github.com/didier-durand) in [#388](https://github.com/jlowin/fastmcp/pull/388)

  ### New Contributors

  * [@didier-durand](https://github.com/didier-durand) made their first contribution in [#385](https://github.com/jlowin/fastmcp/pull/385)

  **Full Changelog**: [v2.3.0...v2.3.1](https://github.com/jlowin/fastmcp/compare/v2.3.0...v2.3.1)
</Update>

<Update label="v2.3.0" description="2024-05-08">
  ## [v2.3.0: Stream Me Up, Scotty](https://github.com/jlowin/fastmcp/releases/tag/v2.3.0)

  ### New Features 🎉

  * Add streaming support for HTTP transport by [@jlowin](https://github.com/jlowin) in [#365](https://github.com/jlowin/fastmcp/pull/365)
  * Support streaming HTTP transport in clients by [@jlowin](https://github.com/jlowin) in [#366](https://github.com/jlowin/fastmcp/pull/366)
  * Add streaming support to CLI by [@jlowin](https://github.com/jlowin) in [#367](https://github.com/jlowin/fastmcp/pull/367)

  ### Fixes 🐞

  * Fix streaming transport initialization by [@jlowin](https://github.com/jlowin) in [#368](https://github.com/jlowin/fastmcp/pull/368)

  ### Docs 📚

  * Update transport documentation for streaming support by [@jlowin](https://github.com/jlowin) in [#369](https://github.com/jlowin/fastmcp/pull/369)

  **Full Changelog**: [v2.2.10...v2.3.0](https://github.com/jlowin/fastmcp/compare/v2.2.10...v2.3.0)
</Update>

<Update label="v2.2.10" description="2024-05-06">
  ## [v2.2.10: That's JSON Bourne](https://github.com/jlowin/fastmcp/releases/tag/v2.2.10)

  ### Fixes 🐞

  * Disable automatic JSON parsing of tool args by [@jlowin](https://github.com/jlowin) in [#341](https://github.com/jlowin/fastmcp/pull/341)
  * Fix prompt test by [@jlowin](https://github.com/jlowin) in [#342](https://github.com/jlowin/fastmcp/pull/342)

  ### Other Changes 🦾

  * Update docs.json by [@jlowin](https://github.com/jlowin) in [#338](https://github.com/jlowin/fastmcp/pull/338)
  * Add test coverage + tests on 4 examples by [@alainivars](https://github.com/alainivars) in [#306](https://github.com/jlowin/fastmcp/pull/306)

  ### New Contributors

  * [@alainivars](https://github.com/alainivars) made their first contribution in [#306](https://github.com/jlowin/fastmcp/pull/306)

  **Full Changelog**: [v2.2.9...v2.2.10](https://github.com/jlowin/fastmcp/compare/v2.2.9...v2.2.10)
</Update>

<Update label="v2.2.9" description="2024-05-06">
  ## [v2.2.9: Str-ing the Pot (Hotfix)](https://github.com/jlowin/fastmcp/releases/tag/v2.2.9)

  This release is a hotfix for the issue detailed in #330

  ### Fixes 🐞

  * Prevent invalid resource URIs by [@jlowin](https://github.com/jlowin) in [#336](https://github.com/jlowin/fastmcp/pull/336)
  * Coerce numbers to str by [@jlowin](https://github.com/jlowin) in [#337](https://github.com/jlowin/fastmcp/pull/337)

  ### Docs 📚

  * Add client badge by [@jlowin](https://github.com/jlowin) in [#327](https://github.com/jlowin/fastmcp/pull/327)
  * Update bug.yml by [@jlowin](https://github.com/jlowin) in [#328](https://github.com/jlowin/fastmcp/pull/328)

  ### Other Changes 🦾

  * Update quickstart.mdx example to include import by [@discdiver](https://github.com/discdiver) in [#329](https://github.com/jlowin/fastmcp/pull/329)

  ### New Contributors

  * [@discdiver](https://github.com/discdiver) made their first contribution in [#329](https://github.com/jlowin/fastmcp/pull/329)

  **Full Changelog**: [v2.2.8...v2.2.9](https://github.com/jlowin/fastmcp/compare/v2.2.8...v2.2.9)
</Update>

<Update label="v2.2.8" description="2024-05-05">
  ## [v2.2.8: Parse and Recreation](https://github.com/jlowin/fastmcp/releases/tag/v2.2.8)

  ### New Features 🎉

  * Replace custom parsing with TypeAdapter by [@jlowin](https://github.com/jlowin) in [#314](https://github.com/jlowin/fastmcp/pull/314)
  * Handle \*args/\*\*kwargs appropriately for various components by [@jlowin](https://github.com/jlowin) in [#317](https://github.com/jlowin/fastmcp/pull/317)
  * Add timeout-graceful-shutdown as a default config for SSE app by [@jlowin](https://github.com/jlowin) in [#323](https://github.com/jlowin/fastmcp/pull/323)
  * Ensure prompts return descriptions by [@jlowin](https://github.com/jlowin) in [#325](https://github.com/jlowin/fastmcp/pull/325)

  ### Fixes 🐞

  * Ensure that tool serialization has a graceful fallback by [@jlowin](https://github.com/jlowin) in [#310](https://github.com/jlowin/fastmcp/pull/310)

  ### Docs 📚

  * Update docs for clarity by [@jlowin](https://github.com/jlowin) in [#312](https://github.com/jlowin/fastmcp/pull/312)

  ### Other Changes 🦾

  * Remove is\_async attribute by [@jlowin](https://github.com/jlowin) in [#315](https://github.com/jlowin/fastmcp/pull/315)
  * Dry out retrieving context kwarg by [@jlowin](https://github.com/jlowin) in [#316](https://github.com/jlowin/fastmcp/pull/316)

  **Full Changelog**: [v2.2.7...v2.2.8](https://github.com/jlowin/fastmcp/compare/v2.2.7...v2.2.8)
</Update>

<Update label="v2.2.7" description="2024-05-03">
  ## [v2.2.7: You Auth to Know Better](https://github.com/jlowin/fastmcp/releases/tag/v2.2.7)

  ### New Features 🎉

  * use pydantic\_core.to\_json by [@jlowin](https://github.com/jlowin) in [#290](https://github.com/jlowin/fastmcp/pull/290)
  * Ensure openapi descriptions are included in tool details by [@jlowin](https://github.com/jlowin) in [#293](https://github.com/jlowin/fastmcp/pull/293)
  * Bump mcp to 1.7.1 by [@jlowin](https://github.com/jlowin) in [#298](https://github.com/jlowin/fastmcp/pull/298)
  * Add support for tool annotations by [@jlowin](https://github.com/jlowin) in [#299](https://github.com/jlowin/fastmcp/pull/299)
  * Add auth support by [@jlowin](https://github.com/jlowin) in [#300](https://github.com/jlowin/fastmcp/pull/300)
  * Add low-level methods to client by [@jlowin](https://github.com/jlowin) in [#301](https://github.com/jlowin/fastmcp/pull/301)
  * Add method for retrieving current starlette request to FastMCP context by [@jlowin](https://github.com/jlowin) in [#302](https://github.com/jlowin/fastmcp/pull/302)
  * get\_starlette\_request → get\_http\_request by [@jlowin](https://github.com/jlowin) in [#303](https://github.com/jlowin/fastmcp/pull/303)
  * Support custom Serializer for Tools by [@strawgate](https://github.com/strawgate) in [#308](https://github.com/jlowin/fastmcp/pull/308)
  * Support proxy mount by [@jlowin](https://github.com/jlowin) in [#309](https://github.com/jlowin/fastmcp/pull/309)

  ### Other Changes 🦾

  * Improve context injection type checks by [@jlowin](https://github.com/jlowin) in [#291](https://github.com/jlowin/fastmcp/pull/291)
  * add readme to smarthome example by [@zzstoatzz](https://github.com/zzstoatzz) in [#294](https://github.com/jlowin/fastmcp/pull/294)

  **Full Changelog**: [v2.2.6...v2.2.7](https://github.com/jlowin/fastmcp/compare/v2.2.6...v2.2.7)
</Update>

<Update label="v2.2.6" description="2024-04-30">
  ## [v2.2.6: The REST is History](https://github.com/jlowin/fastmcp/releases/tag/v2.2.6)

  ### New Features 🎉

  * Added feature : Load MCP server using config by [@sandipan1](https://github.com/sandipan1) in [#260](https://github.com/jlowin/fastmcp/pull/260)
  * small typing fixes by [@zzstoatzz](https://github.com/zzstoatzz) in [#237](https://github.com/jlowin/fastmcp/pull/237)
  * Expose configurable timeout for OpenAPI by [@jlowin](https://github.com/jlowin) in [#279](https://github.com/jlowin/fastmcp/pull/279)
  * Lower websockets pin for compatibility by [@jlowin](https://github.com/jlowin) in [#286](https://github.com/jlowin/fastmcp/pull/286)
  * Improve OpenAPI param handling by [@jlowin](https://github.com/jlowin) in [#287](https://github.com/jlowin/fastmcp/pull/287)

  ### Fixes 🐞

  * Ensure openapi tool responses are properly converted by [@jlowin](https://github.com/jlowin) in [#283](https://github.com/jlowin/fastmcp/pull/283)
  * Fix OpenAPI examples by [@jlowin](https://github.com/jlowin) in [#285](https://github.com/jlowin/fastmcp/pull/285)
  * Fix client docs for advanced features, add tests for logging by [@jlowin](https://github.com/jlowin) in [#284](https://github.com/jlowin/fastmcp/pull/284)

  ### Other Changes 🦾

  * add testing doc by [@jlowin](https://github.com/jlowin) in [#264](https://github.com/jlowin/fastmcp/pull/264)
  * \#267 Fix openapi template resource to support multiple path parameters by [@jeger-at](https://github.com/jeger-at) in [#278](https://github.com/jlowin/fastmcp/pull/278)

  ### New Contributors

  * [@sandipan1](https://github.com/sandipan1) made their first contribution in [#260](https://github.com/jlowin/fastmcp/pull/260)
  * [@jeger-at](https://github.com/jeger-at) made their first contribution in [#278](https://github.com/jlowin/fastmcp/pull/278)

  **Full Changelog**: [v2.2.5...v2.2.6](https://github.com/jlowin/fastmcp/compare/v2.2.5...v2.2.6)
</Update>

<Update label="v2.2.5" description="2024-04-26">
  ## [v2.2.5: Context Switching](https://github.com/jlowin/fastmcp/releases/tag/v2.2.5)

  ### New Features 🎉

  * Add tests for tool return types; improve serialization behavior by [@jlowin](https://github.com/jlowin) in [#262](https://github.com/jlowin/fastmcp/pull/262)
  * Support context injection in resources, templates, and prompts (like tools) by [@jlowin](https://github.com/jlowin) in [#263](https://github.com/jlowin/fastmcp/pull/263)

  ### Docs 📚

  * Update wildcards to 2.2.4 by [@jlowin](https://github.com/jlowin) in [#257](https://github.com/jlowin/fastmcp/pull/257)
  * Update note in templates docs by [@jlowin](https://github.com/jlowin) in [#258](https://github.com/jlowin/fastmcp/pull/258)
  * Significant documentation and test expansion for tool input types by [@jlowin](https://github.com/jlowin) in [#261](https://github.com/jlowin/fastmcp/pull/261)

  **Full Changelog**: [v2.2.4...v2.2.5](https://github.com/jlowin/fastmcp/compare/v2.2.4...v2.2.5)
</Update>

<Update label="v2.2.4" description="2024-04-25">
  ## [v2.2.4: The Wild Side, Actually](https://github.com/jlowin/fastmcp/releases/tag/v2.2.4)

  The wildcard URI templates exposed in v2.2.3 were blocked by a server-level check which is removed in this release.

  ### New Features 🎉

  * Allow customization of inspector proxy port, ui port, and version by [@jlowin](https://github.com/jlowin) in [#253](https://github.com/jlowin/fastmcp/pull/253)

  ### Fixes 🐞

  * fix: unintended type convert by [@cutekibry](https://github.com/cutekibry) in [#252](https://github.com/jlowin/fastmcp/pull/252)
  * Ensure openapi resources return valid responses by [@jlowin](https://github.com/jlowin) in [#254](https://github.com/jlowin/fastmcp/pull/254)
  * Ensure servers expose template wildcards by [@jlowin](https://github.com/jlowin) in [#256](https://github.com/jlowin/fastmcp/pull/256)

  ### Docs 📚

  * Update README.md Grammar error by [@TechWithTy](https://github.com/TechWithTy) in [#249](https://github.com/jlowin/fastmcp/pull/249)

  ### Other Changes 🦾

  * Add resource template tests by [@jlowin](https://github.com/jlowin) in [#255](https://github.com/jlowin/fastmcp/pull/255)

  ### New Contributors

  * [@TechWithTy](https://github.com/TechWithTy) made their first contribution in [#249](https://github.com/jlowin/fastmcp/pull/249)
  * [@cutekibry](https://github.com/cutekibry) made their first contribution in [#252](https://github.com/jlowin/fastmcp/pull/252)

  **Full Changelog**: [v2.2.3...v2.2.4](https://github.com/jlowin/fastmcp/compare/v2.2.3...v2.2.4)
</Update>

<Update label="v2.2.3" description="2024-04-25">
  ## [v2.2.3: The Wild Side](https://github.com/jlowin/fastmcp/releases/tag/v2.2.3)

  ### New Features 🎉

  * Add wildcard params for resource templates by [@jlowin](https://github.com/jlowin) in [#246](https://github.com/jlowin/fastmcp/pull/246)

  ### Docs 📚

  * Indicate that Image class is for returns by [@jlowin](https://github.com/jlowin) in [#242](https://github.com/jlowin/fastmcp/pull/242)
  * Update mermaid diagram by [@jlowin](https://github.com/jlowin) in [#243](https://github.com/jlowin/fastmcp/pull/243)

  ### Other Changes 🦾

  * update version badges by [@jlowin](https://github.com/jlowin) in [#248](https://github.com/jlowin/fastmcp/pull/248)

  **Full Changelog**: [v2.2.2...v2.2.3](https://github.com/jlowin/fastmcp/compare/v2.2.2...v2.2.3)
</Update>

<Update label="v2.2.2" description="2024-04-24">
  ## [v2.2.2: Prompt and Circumstance](https://github.com/jlowin/fastmcp/releases/tag/v2.2.2)

  ### New Features 🎉

  * Add prompt support by [@jlowin](https://github.com/jlowin) in [#235](https://github.com/jlowin/fastmcp/pull/235)

  ### Fixes 🐞

  * Ensure that resource templates are properly exposed by [@jlowin](https://github.com/jlowin) in [#238](https://github.com/jlowin/fastmcp/pull/238)

  ### Docs 📚

  * Update docs for prompts by [@jlowin](https://github.com/jlowin) in [#236](https://github.com/jlowin/fastmcp/pull/236)

  ### Other Changes 🦾

  * Add prompt tests by [@jlowin](https://github.com/jlowin) in [#239](https://github.com/jlowin/fastmcp/pull/239)

  **Full Changelog**: [v2.2.1...v2.2.2](https://github.com/jlowin/fastmcp/compare/v2.2.1...v2.2.2)
</Update>

<Update label="v2.2.1" description="2024-04-23">
  ## [v2.2.1: Template for Success](https://github.com/jlowin/fastmcp/releases/tag/v2.2.1)

  ### New Features 🎉

  * Add resource templates by [@jlowin](https://github.com/jlowin) in [#230](https://github.com/jlowin/fastmcp/pull/230)

  ### Fixes 🐞

  * Ensure that resource templates are properly exposed by [@jlowin](https://github.com/jlowin) in [#231](https://github.com/jlowin/fastmcp/pull/231)

  ### Docs 📚

  * Update docs for resource templates by [@jlowin](https://github.com/jlowin) in [#232](https://github.com/jlowin/fastmcp/pull/232)

  ### Other Changes 🦾

  * Add resource template tests by [@jlowin](https://github.com/jlowin) in [#233](https://github.com/jlowin/fastmcp/pull/233)

  **Full Changelog**: [v2.2.0...v2.2.1](https://github.com/jlowin/fastmcp/compare/v2.2.0...v2.2.1)
</Update>

<Update label="v2.2.0" description="2024-04-22">
  ## [v2.2.0: Compose Yourself](https://github.com/jlowin/fastmcp/releases/tag/v2.2.0)

  ### New Features 🎉

  * Add support for mounting FastMCP servers by [@jlowin](https://github.com/jlowin) in [#175](https://github.com/jlowin/fastmcp/pull/175)
  * Add support for duplicate behavior == ignore by [@jlowin](https://github.com/jlowin) in [#169](https://github.com/jlowin/fastmcp/pull/169)

  ### Breaking Changes 🛫

  * Refactor MCP composition by [@jlowin](https://github.com/jlowin) in [#176](https://github.com/jlowin/fastmcp/pull/176)

  ### Docs 📚

  * Improve integration documentation by [@jlowin](https://github.com/jlowin) in [#184](https://github.com/jlowin/fastmcp/pull/184)
  * Improve documentation by [@jlowin](https://github.com/jlowin) in [#185](https://github.com/jlowin/fastmcp/pull/185)

  ### Other Changes 🦾

  * Add transport kwargs for mcp.run() and fastmcp run by [@jlowin](https://github.com/jlowin) in [#161](https://github.com/jlowin/fastmcp/pull/161)
  * Allow resource templates to have optional / excluded arguments by [@jlowin](https://github.com/jlowin) in [#164](https://github.com/jlowin/fastmcp/pull/164)
  * Update resources.mdx by [@jlowin](https://github.com/jlowin) in [#165](https://github.com/jlowin/fastmcp/pull/165)

  ### New Contributors

  * [@kongqi404](https://github.com/kongqi404) made their first contribution in [#181](https://github.com/jlowin/fastmcp/pull/181)

  **Full Changelog**: [v2.1.2...v2.2.0](https://github.com/jlowin/fastmcp/compare/v2.1.2...v2.2.0)
</Update>

<Update label="v2.1.2" description="2024-04-14">
  ## [v2.1.2: Copy That, Good Buddy](https://github.com/jlowin/fastmcp/releases/tag/v2.1.2)

  The main improvement in this release is a fix that allows FastAPI / OpenAPI-generated servers to be mounted as sub-servers.

  ### Fixes 🐞

  * Ensure objects are copied properly and test mounting fastapi by [@jlowin](https://github.com/jlowin) in [#153](https://github.com/jlowin/fastmcp/pull/153)

  ### Docs 📚

  * Fix broken links in docs by [@jlowin](https://github.com/jlowin) in [#154](https://github.com/jlowin/fastmcp/pull/154)

  ### Other Changes 🦾

  * Update README.md by [@jlowin](https://github.com/jlowin) in [#149](https://github.com/jlowin/fastmcp/pull/149)
  * Only apply log config to FastMCP loggers by [@jlowin](https://github.com/jlowin) in [#155](https://github.com/jlowin/fastmcp/pull/155)
  * Update pyproject.toml by [@jlowin](https://github.com/jlowin) in [#156](https://github.com/jlowin/fastmcp/pull/156)

  **Full Changelog**: [v2.1.1...v2.1.2](https://github.com/jlowin/fastmcp/compare/v2.1.1...v2.1.2)
</Update>

<Update label="v2.1.1" description="2024-04-14">
  ## [v2.1.1: Doc Holiday](https://github.com/jlowin/fastmcp/releases/tag/v2.1.1)

  FastMCP's docs are now available at gofastmcp.com.

  ### Docs 📚

  * Add docs by [@jlowin](https://github.com/jlowin) in [#136](https://github.com/jlowin/fastmcp/pull/136)
  * Add docs link to readme by [@jlowin](https://github.com/jlowin) in [#137](https://github.com/jlowin/fastmcp/pull/137)
  * Minor docs updates by [@jlowin](https://github.com/jlowin) in [#138](https://github.com/jlowin/fastmcp/pull/138)

  ### Fixes 🐞

  * fix branch name in example by [@zzstoatzz](https://github.com/zzstoatzz) in [#140](https://github.com/jlowin/fastmcp/pull/140)

  ### Other Changes 🦾

  * smart home example by [@zzstoatzz](https://github.com/zzstoatzz) in [#115](https://github.com/jlowin/fastmcp/pull/115)
  * Remove mac os tests by [@jlowin](https://github.com/jlowin) in [#142](https://github.com/jlowin/fastmcp/pull/142)
  * Expand support for various method interactions by [@jlowin](https://github.com/jlowin) in [#143](https://github.com/jlowin/fastmcp/pull/143)
  * Update docs and add\_resource\_fn by [@jlowin](https://github.com/jlowin) in [#144](https://github.com/jlowin/fastmcp/pull/144)
  * Update description by [@jlowin](https://github.com/jlowin) in [#145](https://github.com/jlowin/fastmcp/pull/145)
  * Support openapi 3.0 and 3.1 by [@jlowin](https://github.com/jlowin) in [#147](https://github.com/jlowin/fastmcp/pull/147)

  **Full Changelog**: [v2.1.0...v2.1.1](https://github.com/jlowin/fastmcp/compare/v2.1.0...v2.1.1)
</Update>

<Update label="v2.1.0" description="2024-04-13">
  ## [v2.1.0: Tag, You're It](https://github.com/jlowin/fastmcp/releases/tag/v2.1.0)

  The primary motivation for this release is the fix in #128 for Claude desktop compatibility, but the primary new feature of this release is per-object tags. Currently these are for bookkeeping only but will become useful in future releases.

  ### New Features 🎉

  * Add tags for all core MCP objects by [@jlowin](https://github.com/jlowin) in [#121](https://github.com/jlowin/fastmcp/pull/121)
  * Ensure that openapi tags are transferred to MCP objects by [@jlowin](https://github.com/jlowin) in [#124](https://github.com/jlowin/fastmcp/pull/124)

  ### Fixes 🐞

  * Change default mounted tool separator from / to \_ by [@jlowin](https://github.com/jlowin) in [#128](https://github.com/jlowin/fastmcp/pull/128)
  * Enter mounted app lifespans by [@jlowin](https://github.com/jlowin) in [#129](https://github.com/jlowin/fastmcp/pull/129)
  * Fix CLI that called mcp instead of fastmcp by [@jlowin](https://github.com/jlowin) in [#128](https://github.com/jlowin/fastmcp/pull/128)

  ### Breaking Changes 🛫

  * Changed configuration for duplicate resources/tools/prompts by [@jlowin](https://github.com/jlowin) in [#121](https://github.com/jlowin/fastmcp/pull/121)
  * Improve client return types by [@jlowin](https://github.com/jlowin) in [#123](https://github.com/jlowin/fastmcp/pull/123)

  ### Other Changes 🦾

  * Add tests for tags in server decorators by [@jlowin](https://github.com/jlowin) in [#122](https://github.com/jlowin/fastmcp/pull/122)
  * Clean up server tests by [@jlowin](https://github.com/jlowin) in [#125](https://github.com/jlowin/fastmcp/pull/125)

  **Full Changelog**: [v2.0.0...v2.1.0](https://github.com/jlowin/fastmcp/compare/v2.0.0...v2.1.0)
</Update>

<Update label="v2.0.0" description="2024-04-11">
  ## [v2.0.0: Second to None](https://github.com/jlowin/fastmcp/releases/tag/v2.0.0)

  ### New Features 🎉

  * Support mounting FastMCP instances as sub-MCPs by [@jlowin](https://github.com/jlowin) in [#99](https://github.com/jlowin/fastmcp/pull/99)
  * Add in-memory client for calling FastMCP servers (and tests) by [@jlowin](https://github.com/jlowin) in [#100](https://github.com/jlowin/fastmcp/pull/100)
  * Add MCP proxy server by [@jlowin](https://github.com/jlowin) in [#105](https://github.com/jlowin/fastmcp/pull/105)
  * Update FastMCP for upstream changes by [@jlowin](https://github.com/jlowin) in [#107](https://github.com/jlowin/fastmcp/pull/107)
  * Generate FastMCP servers from OpenAPI specs and FastAPI by [@jlowin](https://github.com/jlowin) in [#110](https://github.com/jlowin/fastmcp/pull/110)
  * Reorganize all client / transports by [@jlowin](https://github.com/jlowin) in [#111](https://github.com/jlowin/fastmcp/pull/111)
  * Add sampling and roots by [@jlowin](https://github.com/jlowin) in [#117](https://github.com/jlowin/fastmcp/pull/117)

  ### Fixes 🐞

  * Fix bug with tools that return lists by [@jlowin](https://github.com/jlowin) in [#116](https://github.com/jlowin/fastmcp/pull/116)

  ### Other Changes 🦾

  * Add back FastMCP CLI by [@jlowin](https://github.com/jlowin) in [#108](https://github.com/jlowin/fastmcp/pull/108)
  * Update Readme for v2 by [@jlowin](https://github.com/jlowin) in [#112](https://github.com/jlowin/fastmcp/pull/112)
  * fix deprecation warnings by [@zzstoatzz](https://github.com/zzstoatzz) in [#113](https://github.com/jlowin/fastmcp/pull/113)
  * Readme by [@jlowin](https://github.com/jlowin) in [#118](https://github.com/jlowin/fastmcp/pull/118)
  * FastMCP 2.0 by [@jlowin](https://github.com/jlowin) in [#119](https://github.com/jlowin/fastmcp/pull/119)

  **Full Changelog**: [v1.0...v2.0.0](https://github.com/jlowin/fastmcp/compare/v1.0...v2.0.0)
</Update>

<Update label="v1.0" description="2024-04-11">
  ## [v1.0: It's Official](https://github.com/jlowin/fastmcp/releases/tag/v1.0)

  This release commemorates FastMCP 1.0, which is included in the official Model Context Protocol SDK:

  ```python
  from mcp.server.fastmcp import FastMCP
  ```

  To the best of my knowledge, v1 is identical to the upstream version included with `mcp`.

  ### Docs 📚

  * Update readme to redirect to the official SDK by [@jlowin](https://github.com/jlowin) in [#79](https://github.com/jlowin/fastmcp/pull/79)

  ### Other Changes 🦾

  * fix: use Mount instead of Route for SSE message handling by [@samihamine](https://github.com/samihamine) in [#77](https://github.com/jlowin/fastmcp/pull/77)

  ### New Contributors

  * [@samihamine](https://github.com/samihamine) made their first contribution in [#77](https://github.com/jlowin/fastmcp/pull/77)

  **Full Changelog**: [v0.4.1...v1.0](https://github.com/jlowin/fastmcp/compare/v0.4.1...v1.0)
</Update>

<Update label="v0.4.1" description="2024-12-09">
  ## [v0.4.1: String Theory](https://github.com/jlowin/fastmcp/releases/tag/v0.4.1)

  ### Fixes 🐞

  * fix: handle strings containing numbers correctly by [@sd2k](https://github.com/sd2k) in [#63](https://github.com/jlowin/fastmcp/pull/63)

  ### Docs 📚

  * patch: Update pyproject.toml license by [@leonkozlowski](https://github.com/leonkozlowski) in [#67](https://github.com/jlowin/fastmcp/pull/67)

  ### Other Changes 🦾

  * Avoid new try\_eval\_type unavailable with older pydantic by [@jurasofish](https://github.com/jurasofish) in [#57](https://github.com/jlowin/fastmcp/pull/57)
  * Decorator typing by [@jurasofish](https://github.com/jurasofish) in [#56](https://github.com/jlowin/fastmcp/pull/56)

  ### New Contributors

  * [@leonkozlowski](https://github.com/leonkozlowski) made their first contribution in [#67](https://github.com/jlowin/fastmcp/pull/67)

  **Full Changelog**: [v0.4.0...v0.4.1](https://github.com/jlowin/fastmcp/compare/v0.4.0...v0.4.1)
</Update>

<Update label="v0.4.0" description="2024-12-05">
  ## [v0.4.0: Nice to MIT You](https://github.com/jlowin/fastmcp/releases/tag/v0.4.0)

  This is a relatively small release in terms of features, but the version is bumped to 0.4 to reflect that the code is being relicensed from Apache 2.0 to MIT. This is to facilitate FastMCP's inclusion in the official MCP SDK.

  ### New Features 🎉

  * Add pyright + tests by [@jlowin](https://github.com/jlowin) in [#52](https://github.com/jlowin/fastmcp/pull/52)
  * add pgvector memory example by [@zzstoatzz](https://github.com/zzstoatzz) in [#49](https://github.com/jlowin/fastmcp/pull/49)

  ### Fixes 🐞

  * fix: use stderr for logging by [@sd2k](https://github.com/sd2k) in [#51](https://github.com/jlowin/fastmcp/pull/51)

  ### Docs 📚

  * Update ai-labeler.yml by [@jlowin](https://github.com/jlowin) in [#48](https://github.com/jlowin/fastmcp/pull/48)
  * Relicense from Apache 2.0 to MIT by [@jlowin](https://github.com/jlowin) in [#54](https://github.com/jlowin/fastmcp/pull/54)

  ### Other Changes 🦾

  * fix warning and flake by [@zzstoatzz](https://github.com/zzstoatzz) in [#47](https://github.com/jlowin/fastmcp/pull/47)

  ### New Contributors

  * [@sd2k](https://github.com/sd2k) made their first contribution in [#51](https://github.com/jlowin/fastmcp/pull/51)

  **Full Changelog**: [v0.3.5...v0.4.0](https://github.com/jlowin/fastmcp/compare/v0.3.5...v0.4.0)
</Update>

<Update label="v0.3.5" description="2024-12-03">
  ## [v0.3.5: Windows of Opportunity](https://github.com/jlowin/fastmcp/releases/tag/v0.3.5)

  This release is highlighted by the ability to handle complex JSON objects as MCP inputs and improved Windows compatibility.

  ### New Features 🎉

  * Set up multiple os tests by [@jlowin](https://github.com/jlowin) in [#44](https://github.com/jlowin/fastmcp/pull/44)
  * Changes to accomodate windows users. by [@justjoehere](https://github.com/justjoehere) in [#42](https://github.com/jlowin/fastmcp/pull/42)
  * Handle complex inputs by [@jurasofish](https://github.com/jurasofish) in [#31](https://github.com/jlowin/fastmcp/pull/31)

  ### Docs 📚

  * Make AI labeler more conservative by [@jlowin](https://github.com/jlowin) in [#46](https://github.com/jlowin/fastmcp/pull/46)

  ### Other Changes 🦾

  * Additional Windows Fixes for Dev running and for importing modules in a server by [@justjoehere](https://github.com/justjoehere) in [#43](https://github.com/jlowin/fastmcp/pull/43)

  ### New Contributors

  * [@justjoehere](https://github.com/justjoehere) made their first contribution in [#42](https://github.com/jlowin/fastmcp/pull/42)
  * [@jurasofish](https://github.com/jurasofish) made their first contribution in [#31](https://github.com/jlowin/fastmcp/pull/31)

  **Full Changelog**: [v0.3.4...v0.3.5](https://github.com/jlowin/fastmcp/compare/v0.3.4...v0.3.5)
</Update>

<Update label="v0.3.4" description="2024-12-02">
  ## [v0.3.4: URL's Well That Ends Well](https://github.com/jlowin/fastmcp/releases/tag/v0.3.4)

  ### Fixes 🐞

  * Handle missing config file when installing by [@jlowin](https://github.com/jlowin) in [#37](https://github.com/jlowin/fastmcp/pull/37)
  * Remove BaseURL reference and use AnyURL by [@jlowin](https://github.com/jlowin) in [#40](https://github.com/jlowin/fastmcp/pull/40)

  **Full Changelog**: [v0.3.3...v0.3.4](https://github.com/jlowin/fastmcp/compare/v0.3.3...v0.3.4)
</Update>

<Update label="v0.3.3" description="2024-12-02">
  ## [v0.3.3: Dependence Day](https://github.com/jlowin/fastmcp/releases/tag/v0.3.3)

  ### New Features 🎉

  * Surge example by [@zzstoatzz](https://github.com/zzstoatzz) in [#29](https://github.com/jlowin/fastmcp/pull/29)
  * Support Python dependencies in Server by [@jlowin](https://github.com/jlowin) in [#34](https://github.com/jlowin/fastmcp/pull/34)

  ### Docs 📚

  * add `Contributing` section to README by [@zzstoatzz](https://github.com/zzstoatzz) in [#32](https://github.com/jlowin/fastmcp/pull/32)

  **Full Changelog**: [v0.3.2...v0.3.3](https://github.com/jlowin/fastmcp/compare/v0.3.2...v0.3.3)
</Update>

<Update label="v0.3.2" date="2024-12-01" description="Green with ENVy">
  ## [v0.3.2: Green with ENVy](https://github.com/jlowin/fastmcp/releases/tag/v0.3.2)

  ### New Features 🎉

  * Support env vars when installing by [@jlowin](https://github.com/jlowin) in [#27](https://github.com/jlowin/fastmcp/pull/27)

  ### Docs 📚

  * Remove top level env var by [@jlowin](https://github.com/jlowin) in [#28](https://github.com/jlowin/fastmcp/pull/28)

  **Full Changelog**: [v0.3.1...v0.3.2](https://github.com/jlowin/fastmcp/compare/v0.3.1...v0.3.2)
</Update>

<Update label="v0.3.1" description="2024-12-01">
  ## [v0.3.1](https://github.com/jlowin/fastmcp/releases/tag/v0.3.1)

  ### New Features 🎉

  * Update README.md by [@jlowin](https://github.com/jlowin) in [#23](https://github.com/jlowin/fastmcp/pull/23)
  * add rich handler and dotenv loading for settings by [@zzstoatzz](https://github.com/zzstoatzz) in [#22](https://github.com/jlowin/fastmcp/pull/22)
  * print exception when server can't start by [@jlowin](https://github.com/jlowin) in [#25](https://github.com/jlowin/fastmcp/pull/25)

  ### Docs 📚

  * Update README.md by [@jlowin](https://github.com/jlowin) in [#24](https://github.com/jlowin/fastmcp/pull/24)

  ### Other Changes 🦾

  * Remove log by [@jlowin](https://github.com/jlowin) in [#26](https://github.com/jlowin/fastmcp/pull/26)

  **Full Changelog**: [v0.3.0...v0.3.1](https://github.com/jlowin/fastmcp/compare/v0.3.0...v0.3.1)
</Update>

<Update label="v0.3.0" description="2024-12-01">
  ## [v0.3.0: Prompt and Circumstance](https://github.com/jlowin/fastmcp/releases/tag/v0.3.0)

  ### New Features 🎉

  * Update README by [@jlowin](https://github.com/jlowin) in [#3](https://github.com/jlowin/fastmcp/pull/3)
  * Make log levels strings by [@jlowin](https://github.com/jlowin) in [#4](https://github.com/jlowin/fastmcp/pull/4)
  * Make content method a function by [@jlowin](https://github.com/jlowin) in [#5](https://github.com/jlowin/fastmcp/pull/5)
  * Add template support by [@jlowin](https://github.com/jlowin) in [#6](https://github.com/jlowin/fastmcp/pull/6)
  * Refactor resources module by [@jlowin](https://github.com/jlowin) in [#7](https://github.com/jlowin/fastmcp/pull/7)
  * Clean up cli imports by [@jlowin](https://github.com/jlowin) in [#8](https://github.com/jlowin/fastmcp/pull/8)
  * Prepare to list templates by [@jlowin](https://github.com/jlowin) in [#11](https://github.com/jlowin/fastmcp/pull/11)
  * Move image to separate module by [@jlowin](https://github.com/jlowin) in [#9](https://github.com/jlowin/fastmcp/pull/9)
  * Add support for request context, progress, logging, etc. by [@jlowin](https://github.com/jlowin) in [#12](https://github.com/jlowin/fastmcp/pull/12)
  * Add context tests and better runtime loads by [@jlowin](https://github.com/jlowin) in [#13](https://github.com/jlowin/fastmcp/pull/13)
  * Refactor tools + resourcemanager by [@jlowin](https://github.com/jlowin) in [#14](https://github.com/jlowin/fastmcp/pull/14)
  * func → fn everywhere by [@jlowin](https://github.com/jlowin) in [#15](https://github.com/jlowin/fastmcp/pull/15)
  * Add support for prompts by [@jlowin](https://github.com/jlowin) in [#16](https://github.com/jlowin/fastmcp/pull/16)
  * Create LICENSE by [@jlowin](https://github.com/jlowin) in [#18](https://github.com/jlowin/fastmcp/pull/18)
  * Update cli file spec by [@jlowin](https://github.com/jlowin) in [#19](https://github.com/jlowin/fastmcp/pull/19)
  * Update readmeUpdate README by [@jlowin](https://github.com/jlowin) in [#20](https://github.com/jlowin/fastmcp/pull/20)
  * Use hatchling for version by [@jlowin](https://github.com/jlowin) in [#21](https://github.com/jlowin/fastmcp/pull/21)

  ### Other Changes 🦾

  * Add echo server by [@jlowin](https://github.com/jlowin) in [#1](https://github.com/jlowin/fastmcp/pull/1)
  * Add github workflows by [@jlowin](https://github.com/jlowin) in [#2](https://github.com/jlowin/fastmcp/pull/2)
  * typing updates by [@zzstoatzz](https://github.com/zzstoatzz) in [#17](https://github.com/jlowin/fastmcp/pull/17)

  ### New Contributors

  * [@jlowin](https://github.com/jlowin) made their first contribution in [#1](https://github.com/jlowin/fastmcp/pull/1)
  * [@zzstoatzz](https://github.com/zzstoatzz) made their first contribution in [#17](https://github.com/jlowin/fastmcp/pull/17)

  **Full Changelog**: [v0.2.0...v0.3.0](https://github.com/jlowin/fastmcp/compare/v0.2.0...v0.3.0)
</Update>

<Update label="v0.2.0" description="2024-11-30">
  ## [v0.2.0](https://github.com/jlowin/fastmcp/releases/tag/v0.2.0)

  **Full Changelog**: [v0.1.0...v0.2.0](https://github.com/jlowin/fastmcp/compare/v0.1.0...v0.2.0)
</Update>

<Update label="v0.1.0" description="2024-11-30">
  ## [v0.1.0](https://github.com/jlowin/fastmcp/releases/tag/v0.1.0)

  The very first release of FastMCP! 🎉

  **Full Changelog**: [Initial commits](https://github.com/jlowin/fastmcp/commits/v0.1.0)
</Update>


# Bearer Token Authentication
Source: https://gofastmcp.com/clients/auth/bearer

Authenticate your FastMCP client with a Bearer token.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.6.0" />

<Tip>
  Bearer Token authentication is only relevant for HTTP-based transports.
</Tip>

You can configure your FastMCP client to use **bearer authentication** by supplying a valid access token. This is most appropriate for service accounts, long-lived API keys, CI/CD, applications where authentication is managed separately, or other non-interactive authentication methods.

A Bearer token is a JSON Web Token (JWT) that is used to authenticate a request. It is most commonly used in the `Authorization` header of an HTTP request, using the `Bearer` scheme:

```http
Authorization: Bearer <token>
```

## Client Usage

The most straightforward way to use a pre-existing Bearer token is to provide it as a string to the `auth` parameter of the `fastmcp.Client` or transport instance. FastMCP will automatically format it correctly for the `Authorization` header and bearer scheme.

<Tip>
  If you're using a string token, do not include the `Bearer` prefix. FastMCP will add it for you.
</Tip>

```python {5}
from fastmcp import Client

async with Client(
    "https://fastmcp.cloud/mcp", 
    auth="<your-token>",
) as client:
    await client.ping()
```

You can also supply a Bearer token to a transport instance, such as `StreamableHttpTransport` or `SSETransport`:

```python {6}
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    "http://fastmcp.cloud/mcp", 
    auth="<your-token>",
)

async with Client(transport) as client:
    await client.ping()
```

## `BearerAuth` Helper

If you prefer to be more explicit and not rely on FastMCP to transform your string token, you can use the `BearerAuth` class yourself, which implements the `httpx.Auth` interface.

```python {6}
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

async with Client(
    "https://fastmcp.cloud/mcp", 
    auth=BearerAuth(token="<your-token>"),
) as client:
    await client.ping()
```

## Custom Headers

If the MCP server expects a custom header or token scheme, you can manually set the client's `headers` instead of using the `auth` parameter by setting them on your transport:

```python {5}
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async with Client(
    transport=StreamableHttpTransport(
        "https://fastmcp.cloud/mcp", 
        headers={"X-API-Key": "<your-token>"},
    ),
) as client:
    await client.ping()
```


# OAuth Authentication
Source: https://gofastmcp.com/clients/auth/oauth

Authenticate your FastMCP client via OAuth 2.1.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.6.0" />

<Tip>
  OAuth authentication is only relevant for HTTP-based transports and requires user interaction via a web browser.
</Tip>

When your FastMCP client needs to access an MCP server protected by OAuth 2.1, and the process requires user interaction (like logging in and granting consent), you should use the Authorization Code Flow. FastMCP provides the `fastmcp.client.auth.OAuth` helper to simplify this entire process.

This flow is common for user-facing applications where the application acts on behalf of the user.

## Client Usage

### Default Configuration

The simplest way to use OAuth is to pass the string `"oauth"` to the `auth` parameter of the `Client` or transport instance. FastMCP will automatically configure the client to use OAuth with default settings:

```python {4}
from fastmcp import Client

# Uses default OAuth settings
async with Client("https://fastmcp.cloud/mcp", auth="oauth") as client:
    await client.ping()
```

### `OAuth` Helper

To fully configure the OAuth flow, use the `OAuth` helper and pass it to the `auth` parameter of the `Client` or transport instance. `OAuth` manages the complexities of the OAuth 2.1 Authorization Code Grant with PKCE (Proof Key for Code Exchange) for enhanced security, and implements the full `httpx.Auth` interface.

```python {2, 4, 6}
from fastmcp import Client
from fastmcp.client.auth import OAuth

oauth = OAuth(mcp_url="https://fastmcp.cloud/mcp")

async with Client("https://fastmcp.cloud/mcp", auth=oauth) as client:
    await client.ping()
```

#### `OAuth` Parameters

* **`mcp_url`** (`str`): The full URL of the target MCP server endpoint. Used to discover OAuth server metadata
* **`scopes`** (`str | list[str]`, optional): OAuth scopes to request. Can be space-separated string or list of strings
* **`client_name`** (`str`, optional): Client name for dynamic registration. Defaults to `"FastMCP Client"`
* **`token_storage_cache_dir`** (`Path`, optional): Token cache directory. Defaults to `~/.fastmcp/oauth-mcp-client-cache/`
* **`additional_client_metadata`** (`dict[str, Any]`, optional): Extra metadata for client registration

## OAuth Flow

The OAuth flow is triggered when you use a FastMCP `Client` configured to use OAuth.

<Steps>
  <Step title="Token Check">
    The client first checks the `token_storage_cache_dir` for existing, valid tokens for the target server. If one is found, it will be used to authenticate the client.
  </Step>

  <Step title="OAuth Server Discovery">
    If no valid tokens exist, the client attempts to discover the OAuth server's endpoints using a well-known URI (e.g., `/.well-known/oauth-authorization-server`) based on the `mcp_url`.
  </Step>

  <Step title="Dynamic Client Registration">
    If the OAuth server supports it and the client isn't already registered (or credentials aren't cached), the client performs dynamic client registration according to RFC 7591.
  </Step>

  <Step title="Local Callback Server">
    A temporary local HTTP server is started on an available port. This server's address (e.g., `http://127.0.0.1:<port>/callback`) acts as the `redirect_uri` for the OAuth flow.
  </Step>

  <Step title="Browser Interaction">
    The user's default web browser is automatically opened, directing them to the OAuth server's authorization endpoint. The user logs in and grants (or denies) the requested `scopes`.
  </Step>

  <Step title="Authorization Code & Token Exchange">
    Upon approval, the OAuth server redirects the user's browser to the local callback server with an `authorization_code`. The client captures this code and exchanges it with the OAuth server's token endpoint for an `access_token` (and often a `refresh_token`) using PKCE for security.
  </Step>

  <Step title="Token Caching">
    The obtained tokens are saved to the `token_storage_cache_dir` for future use, eliminating the need for repeated browser interactions.
  </Step>

  <Step title="Authenticated Requests">
    The access token is automatically included in the `Authorization` header for requests to the MCP server.
  </Step>

  <Step title="Refresh Token">
    If the access token expires, the client will automatically use the refresh token to get a new access token.
  </Step>
</Steps>

## Token Management

### Token Storage

OAuth access tokens are automatically cached in `~/.fastmcp/oauth-mcp-client-cache/` and persist between application runs. Files are keyed by the OAuth server's base URL.

### Managing Cache

To clear the tokens for a specific server, instantiate a `FileTokenStorage` instance and call the `clear` method:

```python
from fastmcp.client.auth.oauth import FileTokenStorage

storage = FileTokenStorage(server_url="https://fastmcp.cloud/mcp")
await storage.clear()
```

To clear *all* tokens for all servers, call the `clear_all` method on the `FileTokenStorage` class:

```python
from fastmcp.client.auth.oauth import FileTokenStorage

FileTokenStorage.clear_all()
```


# The FastMCP Client
Source: https://gofastmcp.com/clients/client

Programmatic client for interacting with MCP servers through a well-typed, Pythonic interface.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

The central piece of MCP client applications is the `fastmcp.Client` class. This class provides a **programmatic interface** for interacting with any Model Context Protocol (MCP) server, handling protocol details and connection management automatically.

The FastMCP Client is designed for deterministic, controlled interactions rather than autonomous behavior, making it ideal for:

* **Testing MCP servers** during development
* **Building deterministic applications** that need reliable MCP interactions
* **Creating the foundation for agentic or LLM-based clients** with structured, type-safe operations

All client operations require using the `async with` context manager for proper connection lifecycle management.

<Note>
  This is not an agentic client - it requires explicit function calls and provides direct control over all MCP operations. Use it as a building block for higher-level systems.
</Note>

## Creating a Client

Creating a client is straightforward. You provide a server source and the client automatically infers the appropriate transport mechanism.

```python
import asyncio
from fastmcp import Client, FastMCP

# In-memory server (ideal for testing)
server = FastMCP("TestServer")
client = Client(server)

# HTTP server
client = Client("https://example.com/mcp")

# Local Python script
client = Client("my_mcp_server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        # Execute operations
        result = await client.call_tool("example_tool", {"param": "value"})
        print(result)

asyncio.run(main())
```

## Client-Transport Architecture

The FastMCP Client separates concerns between protocol and connection:

* **`Client`**: Handles MCP protocol operations (tools, resources, prompts) and manages callbacks
* **`Transport`**: Establishes and maintains the connection (WebSockets, HTTP, Stdio, in-memory)

### Transport Inference

The client automatically infers the appropriate transport based on the input:

1. **`FastMCP` instance** → In-memory transport (perfect for testing)
2. **File path ending in `.py`** → Python Stdio transport
3. **File path ending in `.js`** → Node.js Stdio transport
4. **URL starting with `http://` or `https://`** → HTTP transport
5. **`MCPConfig` dictionary** → Multi-server client

```python
from fastmcp import Client, FastMCP

# Examples of transport inference
client_memory = Client(FastMCP("TestServer"))
client_script = Client("./server.py") 
client_http = Client("https://api.example.com/mcp")
```

<Tip>
  For testing and development, always prefer the in-memory transport by passing a `FastMCP` server directly to the client. This eliminates network complexity and separate processes.
</Tip>

## Configuration-Based Clients

<VersionBadge version="2.4.0" />

Create clients from MCP configuration dictionaries, which can include multiple servers. While there is no official standard for MCP configuration format, FastMCP follows established conventions used by tools like Claude Desktop.

### Configuration Format

```python
config = {
    "mcpServers": {
        "server_name": {
            # Remote HTTP/SSE server
            "transport": "http",  # or "sse" 
            "url": "https://api.example.com/mcp",
            "headers": {"Authorization": "Bearer token"},
            "auth": "oauth"  # or bearer token string
        },
        "local_server": {
            # Local stdio server
            "transport": "stdio",
            "command": "python",
            "args": ["./server.py", "--verbose"],
            "env": {"DEBUG": "true"},
            "cwd": "/path/to/server",
        }
    }
}
```

### Multi-Server Example

```python
config = {
    "mcpServers": {
        "weather": {"url": "https://weather-api.example.com/mcp"},
        "assistant": {"command": "python", "args": ["./assistant_server.py"]}
    }
}

client = Client(config)

async with client:
    # Tools are prefixed with server names
    weather_data = await client.call_tool("weather_get_forecast", {"city": "London"})
    response = await client.call_tool("assistant_answer_question", {"question": "What's the capital of France?"})
    
    # Resources use prefixed URIs
    icons = await client.read_resource("weather://weather/icons/sunny")
    templates = await client.read_resource("resource://assistant/templates/list")
```

## Connection Lifecycle

The client operates asynchronously and uses context managers for connection management:

```python
async def example():
    client = Client("my_mcp_server.py")
    
    # Connection established here
    async with client:
        print(f"Connected: {client.is_connected()}")
        
        # Make multiple calls within the same session
        tools = await client.list_tools()
        result = await client.call_tool("greet", {"name": "World"})
        
    # Connection closed automatically here
    print(f"Connected: {client.is_connected()}")
```

## Operations

FastMCP clients can interact with several types of server components:

### Tools

Tools are server-side functions that the client can execute with arguments.

```python
async with client:
    # List available tools
    tools = await client.list_tools()
    
    # Execute a tool
    result = await client.call_tool("multiply", {"a": 5, "b": 3})
    print(result.data)  # 15
```

See [Tools](/clients/tools) for detailed documentation.

### Resources

Resources are data sources that the client can read, either static or templated.

```python
async with client:
    # List available resources
    resources = await client.list_resources()
    
    # Read a resource
    content = await client.read_resource("file:///config/settings.json")
    print(content[0].text)
```

See [Resources](/clients/resources) for detailed documentation.

### Prompts

Prompts are reusable message templates that can accept arguments.

```python
async with client:
    # List available prompts
    prompts = await client.list_prompts()
    
    # Get a rendered prompt
    messages = await client.get_prompt("analyze_data", {"data": [1, 2, 3]})
    print(messages.messages)
```

See [Prompts](/clients/prompts) for detailed documentation.

### Server Connectivity

Use `ping()` to verify the server is reachable:

```python
async with client:
    await client.ping()
    print("Server is reachable")
```

## Client Configuration

Clients can be configured with additional handlers and settings for specialized use cases.

### Callback Handlers

The client supports several callback handlers for advanced server interactions:

```python
from fastmcp import Client
from fastmcp.client.logging import LogMessage

async def log_handler(message: LogMessage):
    print(f"Server log: {message.data}")

async def progress_handler(progress: float, total: float | None, message: str | None):
    print(f"Progress: {progress}/{total} - {message}")

async def sampling_handler(messages, params, context):
    # Integrate with your LLM service here
    return "Generated response"

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
    progress_handler=progress_handler,
    sampling_handler=sampling_handler,
    timeout=30.0
)
```

The `Client` constructor accepts several configuration options:

* `transport`: Transport instance or source for automatic inference
* `log_handler`: Handle server log messages
* `progress_handler`: Monitor long-running operations
* `sampling_handler`: Respond to server LLM requests
* `roots`: Provide local context to servers
* `timeout`: Default timeout for requests (in seconds)

### Transport Configuration

For detailed transport configuration (headers, authentication, environment variables), see the [Transports](/clients/transports) documentation.

## Next Steps

Explore the detailed documentation for each operation type:

### Core Operations

* **[Tools](/clients/tools)** - Execute server-side functions and handle results
* **[Resources](/clients/resources)** - Access static and templated resources
* **[Prompts](/clients/prompts)** - Work with message templates and argument serialization

### Advanced Features

* **[Logging](/clients/logging)** - Handle server log messages
* **[Progress](/clients/progress)** - Monitor long-running operations
* **[Sampling](/clients/sampling)** - Respond to server LLM requests
* **[Roots](/clients/roots)** - Provide local context to servers

### Connection Details

* **[Transports](/clients/transports)** - Configure connection methods and parameters
* **[Authentication](/clients/auth/oauth)** - Set up OAuth and bearer token authentication

<Tip>
  The FastMCP Client is designed as a foundational tool. Use it directly for deterministic operations, or build higher-level agentic systems on top of its reliable, type-safe interface.
</Tip>


# User Elicitation
Source: https://gofastmcp.com/clients/elicitation

Handle server-initiated user input requests with structured schemas.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.10.0" />

## What is Elicitation?

Elicitation allows MCP servers to request structured input from users during tool execution. Instead of requiring all inputs upfront, servers can interactively ask users for information as needed - like prompting for missing parameters, requesting clarification, or gathering additional context.

For example, a file management tool might ask "Which directory should I create?" or a data analysis tool might request "What date range should I analyze?"

## How FastMCP Makes Elicitation Easy

FastMCP's client provides a helpful abstraction layer that:

* **Converts JSON schemas to Python types**: The raw MCP protocol uses JSON schemas, but FastMCP automatically converts these to Python dataclasses
* **Provides structured constructors**: Instead of manually building dictionaries that match the schema, you get dataclass constructors that ensure correct structure
* **Handles type conversion**: FastMCP takes care of converting between JSON representations and Python objects
* **Runtime introspection**: You can inspect the generated dataclass fields to understand the expected structure

When you implement an elicitation handler, FastMCP gives you a dataclass type that matches the server's schema, making it easy to create properly structured responses without having to manually parse JSON schemas.

## Elicitation Handler

Provide an `elicitation_handler` function when creating the client. FastMCP automatically converts the server's JSON schema into a Python dataclass type, making it easy to construct the response:

```python
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def elicitation_handler(message: str, response_type: type, params, context):
    # Present the message to the user and collect input
    user_input = input(f"{message}: ")
    
    # Create response using the provided dataclass type
    # FastMCP converted the JSON schema to this Python type for you
    response_data = response_type(value=user_input)
    
    # You can return data directly - FastMCP will implicitly accept the elicitation
    return response_data
    
    # Or explicitly return an ElicitResult for more control
    # return ElicitResult(action="accept", content=response_data)

client = Client(
    "my_mcp_server.py",
    elicitation_handler=elicitation_handler,
)
```

### Handler Parameters

The elicitation handler receives four parameters:

<Card icon="code" title="Elicitation Handler Parameters">
  <ResponseField name="message" type="str">
    The prompt message to display to the user
  </ResponseField>

  <ResponseField name="response_type" type="type">
    A Python dataclass type that FastMCP created from the server's JSON schema. Use this to construct your response with proper typing and IDE support. If the server requests an empty object (indicating no response), this will be `None`.
  </ResponseField>

  <ResponseField name="params" type="ElicitRequestParams">
    The original MCP elicitation request parameters, including the raw JSON schema in `params.requestedSchema` if you need it
  </ResponseField>

  <ResponseField name="context" type="RequestContext">
    Request context containing metadata about the elicitation request
  </ResponseField>
</Card>

### Response Actions

The handler can return data directly (which implicitly accepts the elicitation) or an `ElicitResult` object for more control over the response action:

<Card icon="code" title="ElicitResult Structure">
  <ResponseField name="action" type="Literal['accept', 'decline', 'cancel']">
    How the user responded to the elicitation request
  </ResponseField>

  <ResponseField name="content" type="dataclass instance | dict | None">
    The user's input data (required for "accept", omitted for "decline"/"cancel")
  </ResponseField>
</Card>

**Action Types:**

* **`accept`**: User provided valid input - include their data in the `content` field
* **`decline`**: User chose not to provide the requested information - omit `content`
* **`cancel`**: User cancelled the entire operation - omit `content`

## Basic Example

```python
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

async def basic_elicitation_handler(message: str, response_type: type, params, context):
    print(f"Server asks: {message}")
    
    # Simple text input for demonstration
    user_response = input("Your response: ")
    
    if not user_response:
        # For non-acceptance, use ElicitResult explicitly
        return ElicitResult(action="decline")
    
    # Use the response_type dataclass to create a properly structured response
    # FastMCP handles the conversion from JSON schema to Python type
    # Return data directly - FastMCP will implicitly accept the elicitation
    return response_type(value=user_response)

client = Client(
    "my_mcp_server.py", 
    elicitation_handler=basic_elicitation_handler
)
```


# Server Logging
Source: https://gofastmcp.com/clients/logging

Receive and handle log messages from MCP servers.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

MCP servers can emit log messages to clients. The client can handle these logs through a log handler callback.

## Log Handler

Provide a `log_handler` function when creating the client:

```python
from fastmcp import Client
from fastmcp.client.logging import LogMessage

async def log_handler(message: LogMessage):
    level = message.level.upper()
    logger = message.logger or 'server'
    data = message.data
    print(f"[{level}] {logger}: {data}")

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
)
```

### Handler Parameters

The `log_handler` is called every time a log message is received. It receives a `LogMessage` object:

<Card icon="code" title="Log Handler Parameters">
  <ResponseField name="LogMessage" type="Log Message Object">
    <Expandable title="attributes">
      <ResponseField name="level" type="Literal[&#x22;debug&#x22;, &#x22;info&#x22;, &#x22;notice&#x22;, &#x22;warning&#x22;, &#x22;error&#x22;, &#x22;critical&#x22;, &#x22;alert&#x22;, &#x22;emergency&#x22;]">
        The log level
      </ResponseField>

      <ResponseField name="logger" type="str | None">
        The logger name (optional, may be None)
      </ResponseField>

      <ResponseField name="data" type="Any">
        The actual log message content
      </ResponseField>
    </Expandable>
  </ResponseField>
</Card>

```python
async def detailed_log_handler(message: LogMessage):
    if message.level == "error":
        print(f"ERROR: {message.data}")
    elif message.level == "warning":
        print(f"WARNING: {message.data}")
    else:
        print(f"{message.level.upper()}: {message.data}")
```

## Default Log Handling

If you don't provide a custom `log_handler`, FastMCP uses a default handler that emits a DEBUG-level FastMCP log for every log message received from the server, which is useful for visibility without polluting your own logs.

```python
client = Client("my_mcp_server.py")

async with client:
    # Server logs will be emitted at DEBUG level automatically
    await client.call_tool("some_tool")
```


# Message Handling
Source: https://gofastmcp.com/clients/messages

Handle MCP messages, requests, and notifications with custom message handlers.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.9.1" />

MCP clients can receive various types of messages from servers, including requests that need responses and notifications that don't. The message handler provides a unified way to process all these messages.

## Function-Based Handler

The simplest way to handle messages is with a function that receives all messages:

```python
from fastmcp import Client

async def message_handler(message):
    """Handle all MCP messages from the server."""
    if hasattr(message, 'root'):
        method = message.root.method
        print(f"Received: {method}")
        
        # Handle specific notifications
        if method == "notifications/tools/list_changed":
            print("Tools have changed - might want to refresh tool cache")
        elif method == "notifications/resources/list_changed":
            print("Resources have changed")

client = Client(
    "my_mcp_server.py",
    message_handler=message_handler,
)
```

## Message Handler Class

For fine-grained targeting, FastMCP provides a `MessageHandler` class you can subclass to take advantage of specific hooks:

```python
from fastmcp import Client
from fastmcp.client.messages import MessageHandler
import mcp.types

class MyMessageHandler(MessageHandler):
    async def on_tool_list_changed(
        self, notification: mcp.types.ToolListChangedNotification
    ) -> None:
        """Handle tool list changes specifically."""
        print("Tool list changed - refreshing available tools")

client = Client(
    "my_mcp_server.py",
    message_handler=MyMessageHandler(),
)
```

### Available Handler Methods

All handler methods receive a single argument - the specific message type:

<Card icon="code" title="Message Handler Methods">
  <ResponseField name="on_message(message)" type="Any MCP message">
    Called for ALL messages (requests and notifications)
  </ResponseField>

  <ResponseField name="on_request(request)" type="mcp.types.ClientRequest">
    Called for requests that expect responses
  </ResponseField>

  <ResponseField name="on_notification(notification)" type="mcp.types.ServerNotification">
    Called for notifications (fire-and-forget)
  </ResponseField>

  <ResponseField name="on_tool_list_changed(notification)" type="mcp.types.ToolListChangedNotification">
    Called when the server's tool list changes
  </ResponseField>

  <ResponseField name="on_resource_list_changed(notification)" type="mcp.types.ResourceListChangedNotification">
    Called when the server's resource list changes
  </ResponseField>

  <ResponseField name="on_prompt_list_changed(notification)" type="mcp.types.PromptListChangedNotification">
    Called when the server's prompt list changes
  </ResponseField>

  <ResponseField name="on_progress(notification)" type="mcp.types.ProgressNotification">
    Called for progress updates during long-running operations
  </ResponseField>

  <ResponseField name="on_logging_message(notification)" type="mcp.types.LoggingMessageNotification">
    Called for log messages from the server
  </ResponseField>
</Card>

## Example: Handling Tool Changes

Here's a practical example of handling tool list changes:

```python
from fastmcp.client.messages import MessageHandler
import mcp.types

class ToolCacheHandler(MessageHandler):
    def __init__(self):
        self.cached_tools = []
    
    async def on_tool_list_changed(
        self, notification: mcp.types.ToolListChangedNotification
    ) -> None:
        """Clear tool cache when tools change."""
        print("Tools changed - clearing cache")
        self.cached_tools = []  # Force refresh on next access

client = Client("server.py", message_handler=ToolCacheHandler())
```

## Handling Requests

While the message handler receives server-initiated requests, for most use cases you should use the dedicated callback parameters instead:

* **Sampling requests**: Use [`sampling_handler`](/clients/sampling)
* **Progress requests**: Use [`progress_handler`](/clients/progress)
* **Log requests**: Use [`log_handler`](/clients/logging)

The message handler is primarily for monitoring and handling notifications rather than responding to requests.


# Progress Monitoring
Source: https://gofastmcp.com/clients/progress

Handle progress notifications from long-running server operations.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.3.5" />

MCP servers can report progress during long-running operations. The client can receive these updates through a progress handler.

## Progress Handler

Set a progress handler when creating the client:

```python
from fastmcp import Client

async def my_progress_handler(
    progress: float, 
    total: float | None, 
    message: str | None
) -> None:
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {percentage:.1f}% - {message or ''}")
    else:
        print(f"Progress: {progress} - {message or ''}")

client = Client(
    "my_mcp_server.py",
    progress_handler=my_progress_handler
)
```

### Handler Parameters

The progress handler receives three parameters:

<Card icon="code" title="Progress Handler Parameters">
  <ResponseField name="progress" type="float">
    Current progress value
  </ResponseField>

  <ResponseField name="total" type="float | None">
    Expected total value (may be None)
  </ResponseField>

  <ResponseField name="message" type="str | None">
    Optional status message (may be None)
  </ResponseField>
</Card>

## Per-Call Progress Handler

Override the progress handler for specific tool calls:

```python
async with client:
    # Override with specific progress handler for this call
    result = await client.call_tool(
        "long_running_task", 
        {"param": "value"}, 
        progress_handler=my_progress_handler
    )
```


# Prompts
Source: https://gofastmcp.com/clients/prompts

Use server-side prompt templates with automatic argument serialization.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

Prompts are reusable message templates exposed by MCP servers. They can accept arguments to generate personalized message sequences for LLM interactions.

## Listing Prompts

Use `list_prompts()` to retrieve all available prompt templates:

```python
async with client:
    prompts = await client.list_prompts()
    # prompts -> list[mcp.types.Prompt]
    
    for prompt in prompts:
        print(f"Prompt: {prompt.name}")
        print(f"Description: {prompt.description}")
        if prompt.arguments:
            print(f"Arguments: {[arg.name for arg in prompt.arguments]}")
```

## Using Prompts

### Basic Usage

Request a rendered prompt using `get_prompt()` with the prompt name and arguments:

```python
async with client:
    # Simple prompt without arguments
    result = await client.get_prompt("welcome_message")
    # result -> mcp.types.GetPromptResult
    
    # Access the generated messages
    for message in result.messages:
        print(f"Role: {message.role}")
        print(f"Content: {message.content}")
```

### Prompts with Arguments

Pass arguments as a dictionary to customize the prompt:

```python
async with client:
    # Prompt with simple arguments
    result = await client.get_prompt("user_greeting", {
        "name": "Alice",
        "role": "administrator"
    })
    
    # Access the personalized messages
    for message in result.messages:
        print(f"Generated message: {message.content}")
```

## Automatic Argument Serialization

<VersionBadge version="2.9.0" />

FastMCP automatically serializes complex arguments to JSON strings as required by the MCP specification. This allows you to pass typed objects directly:

```python
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int

async with client:
    # Complex arguments are automatically serialized
    result = await client.get_prompt("analyze_user", {
        "user": UserData(name="Alice", age=30),     # Automatically serialized to JSON
        "preferences": {"theme": "dark"},           # Dict serialized to JSON string
        "scores": [85, 92, 78],                     # List serialized to JSON string
        "simple_name": "Bob"                        # Strings passed through unchanged
    })
```

The client handles serialization using `pydantic_core.to_json()` for consistent formatting. FastMCP servers can automatically deserialize these JSON strings back to the expected types.

### Serialization Examples

```python
async with client:
    result = await client.get_prompt("data_analysis", {
        # These will be automatically serialized to JSON strings:
        "config": {
            "format": "csv",
            "include_headers": True,
            "delimiter": ","
        },
        "filters": [
            {"field": "age", "operator": ">", "value": 18},
            {"field": "status", "operator": "==", "value": "active"}
        ],
        # This remains a string:
        "report_title": "Monthly Analytics Report"
    })
```

## Working with Prompt Results

The `get_prompt()` method returns a `GetPromptResult` object containing a list of messages:

```python
async with client:
    result = await client.get_prompt("conversation_starter", {"topic": "climate"})
    
    # Access individual messages
    for i, message in enumerate(result.messages):
        print(f"Message {i + 1}:")
        print(f"  Role: {message.role}")
        print(f"  Content: {message.content.text if hasattr(message.content, 'text') else message.content}")
```

## Raw MCP Protocol Access

For access to the complete MCP protocol objects, use the `*_mcp` methods:

```python
async with client:
    # Raw MCP method returns full protocol object
    prompts_result = await client.list_prompts_mcp()
    # prompts_result -> mcp.types.ListPromptsResult
    
    prompt_result = await client.get_prompt_mcp("example_prompt", {"arg": "value"})
    # prompt_result -> mcp.types.GetPromptResult
```

## Multi-Server Clients

When using multi-server clients, prompts are accessible without prefixing (unlike tools):

```python
async with client:  # Multi-server client
    # Prompts from any server are directly accessible
    result1 = await client.get_prompt("weather_prompt", {"city": "London"})
    result2 = await client.get_prompt("assistant_prompt", {"query": "help"})
```

## Common Prompt Patterns

### System Messages

Many prompts generate system messages for LLM configuration:

```python
async with client:
    result = await client.get_prompt("system_configuration", {
        "role": "helpful assistant",
        "expertise": "python programming"
    })
    
    # Typically returns messages with role="system"
    system_message = result.messages[0]
    print(f"System prompt: {system_message.content}")
```

### Conversation Templates

Prompts can generate multi-turn conversation templates:

```python
async with client:
    result = await client.get_prompt("interview_template", {
        "candidate_name": "Alice",
        "position": "Senior Developer"
    })
    
    # Multiple messages for a conversation flow
    for message in result.messages:
        print(f"{message.role}: {message.content}")
```

<Tip>
  Prompt arguments and their expected types depend on the specific prompt implementation. Check the server's documentation or use `list_prompts()` to see available arguments for each prompt.
</Tip>


# Resource Operations
Source: https://gofastmcp.com/clients/resources

Access static and templated resources from MCP servers.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

Resources are data sources exposed by MCP servers. They can be static files or dynamic templates that generate content based on parameters.

## Types of Resources

MCP servers expose two types of resources:

* **Static Resources**: Fixed content accessible via URI (e.g., configuration files, documentation)
* **Resource Templates**: Dynamic resources that accept parameters to generate content (e.g., API endpoints, database queries)

## Listing Resources

### Static Resources

Use `list_resources()` to retrieve all static resources available on the server:

```python
async with client:
    resources = await client.list_resources()
    # resources -> list[mcp.types.Resource]
    
    for resource in resources:
        print(f"Resource URI: {resource.uri}")
        print(f"Name: {resource.name}")
        print(f"Description: {resource.description}")
        print(f"MIME Type: {resource.mimeType}")
```

### Resource Templates

Use `list_resource_templates()` to retrieve available resource templates:

```python
async with client:
    templates = await client.list_resource_templates()
    # templates -> list[mcp.types.ResourceTemplate]
    
    for template in templates:
        print(f"Template URI: {template.uriTemplate}")
        print(f"Name: {template.name}")
        print(f"Description: {template.description}")
```

## Reading Resources

### Static Resources

Read a static resource using its URI:

```python
async with client:
    # Read a static resource
    content = await client.read_resource("file:///path/to/README.md")
    # content -> list[mcp.types.TextResourceContents | mcp.types.BlobResourceContents]
    
    # Access text content
    if hasattr(content[0], 'text'):
        print(content[0].text)
    
    # Access binary content
    if hasattr(content[0], 'blob'):
        print(f"Binary data: {len(content[0].blob)} bytes")
```

### Resource Templates

Read from a resource template by providing the URI with parameters:

```python
async with client:
    # Read a resource generated from a template
    # For example, a template like "weather://{{city}}/current"
    weather_content = await client.read_resource("weather://london/current")
    
    # Access the generated content
    print(weather_content[0].text)  # Assuming text JSON response
```

## Content Types

Resources can return different content types:

### Text Resources

```python
async with client:
    content = await client.read_resource("resource://config/settings.json")
    
    for item in content:
        if hasattr(item, 'text'):
            print(f"Text content: {item.text}")
            print(f"MIME type: {item.mimeType}")
```

### Binary Resources

```python
async with client:
    content = await client.read_resource("resource://images/logo.png")
    
    for item in content:
        if hasattr(item, 'blob'):
            print(f"Binary content: {len(item.blob)} bytes")
            print(f"MIME type: {item.mimeType}")
            
            # Save to file
            with open("downloaded_logo.png", "wb") as f:
                f.write(item.blob)
```

## Working with Multi-Server Clients

When using multi-server clients, resource URIs are automatically prefixed with the server name:

```python
async with client:  # Multi-server client
    # Access resources from different servers
    weather_icons = await client.read_resource("weather://weather/icons/sunny")
    templates = await client.read_resource("resource://assistant/templates/list")
    
    print(f"Weather icon: {weather_icons[0].blob}")
    print(f"Templates: {templates[0].text}")
```

## Raw MCP Protocol Access

For access to the complete MCP protocol objects, use the `*_mcp` methods:

```python
async with client:
    # Raw MCP methods return full protocol objects
    resources_result = await client.list_resources_mcp()
    # resources_result -> mcp.types.ListResourcesResult
    
    templates_result = await client.list_resource_templates_mcp()
    # templates_result -> mcp.types.ListResourceTemplatesResult
    
    content_result = await client.read_resource_mcp("resource://example")
    # content_result -> mcp.types.ReadResourceResult
```

## Common Resource URI Patterns

Different MCP servers may use various URI schemes:

```python
# File system resources
"file:///path/to/file.txt"

# Custom protocol resources  
"weather://london/current"
"database://users/123"

# Generic resource protocol
"resource://config/settings"
"resource://templates/email"
```

<Tip>
  Resource URIs and their formats depend on the specific MCP server implementation. Check the server's documentation for available resources and their URI patterns.
</Tip>


# Client Roots
Source: https://gofastmcp.com/clients/roots

Provide local context and resource boundaries to MCP servers.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

Roots are a way for clients to inform servers about the resources they have access to. Servers can use this information to adjust behavior or provide more relevant responses.

## Setting Static Roots

Provide a list of roots when creating the client:

<CodeGroup>
  ```python Static Roots
  from fastmcp import Client

  client = Client(
      "my_mcp_server.py", 
      roots=["/path/to/root1", "/path/to/root2"]
  )
  ```

  ```python Dynamic Roots Callback
  from fastmcp import Client
  from fastmcp.client.roots import RequestContext

  async def roots_callback(context: RequestContext) -> list[str]:
      print(f"Server requested roots (Request ID: {context.request_id})")
      return ["/path/to/root1", "/path/to/root2"]

  client = Client(
      "my_mcp_server.py", 
      roots=roots_callback
  )
  ```
</CodeGroup>


# LLM Sampling
Source: https://gofastmcp.com/clients/sampling

Handle server-initiated LLM sampling requests.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

MCP servers can request LLM completions from clients. The client handles these requests through a sampling handler callback.

## Sampling Handler

Provide a `sampling_handler` function when creating the client:

```python
from fastmcp import Client
from fastmcp.client.sampling import (
    SamplingMessage,
    SamplingParams,
    RequestContext,
)

async def sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    # Your LLM integration logic here
    # Extract text from messages and generate a response
    return "Generated response based on the messages"

client = Client(
    "my_mcp_server.py",
    sampling_handler=sampling_handler,
)
```

### Handler Parameters

The sampling handler receives three parameters:

<Card icon="code" title="Sampling Handler Parameters">
  <ResponseField name="SamplingMessage" type="Sampling Message Object">
    <Expandable title="attributes">
      <ResponseField name="role" type="Literal[&#x22;user&#x22;, &#x22;assistant&#x22;]">
        The role of the message.
      </ResponseField>

      <ResponseField name="content" type="TextContent | ImageContent | AudioContent">
        The content of the message.

        TextContent is most common, and has a `.text` attribute.
      </ResponseField>
    </Expandable>
  </ResponseField>

  <ResponseField name="SamplingParams" type="Sampling Parameters Object">
    <Expandable title="attributes">
      <ResponseField name="messages" type="list[SamplingMessage]">
        The messages to sample from
      </ResponseField>

      <ResponseField name="modelPreferences" type="ModelPreferences | None">
        The server's preferences for which model to select. The client MAY ignore
        these preferences.

        <Expandable title="attributes">
          <ResponseField name="hints" type="list[ModelHint] | None">
            The hints to use for model selection.
          </ResponseField>

          <ResponseField name="costPriority" type="float | None">
            The cost priority for model selection.
          </ResponseField>

          <ResponseField name="speedPriority" type="float | None">
            The speed priority for model selection.
          </ResponseField>

          <ResponseField name="intelligencePriority" type="float | None">
            The intelligence priority for model selection.
          </ResponseField>
        </Expandable>
      </ResponseField>

      <ResponseField name="systemPrompt" type="str | None">
        An optional system prompt the server wants to use for sampling.
      </ResponseField>

      <ResponseField name="includeContext" type="IncludeContext | None">
        A request to include context from one or more MCP servers (including the caller), to
        be attached to the prompt.
      </ResponseField>

      <ResponseField name="temperature" type="float | None">
        The sampling temperature.
      </ResponseField>

      <ResponseField name="maxTokens" type="int">
        The maximum number of tokens to sample.
      </ResponseField>

      <ResponseField name="stopSequences" type="list[str] | None">
        The stop sequences to use for sampling.
      </ResponseField>

      <ResponseField name="metadata" type="dict[str, Any] | None">
        Optional metadata to pass through to the LLM provider.
      </ResponseField>
    </Expandable>
  </ResponseField>

  <ResponseField name="RequestContext" type="Request Context Object">
    <Expandable title="attributes">
      <ResponseField name="request_id" type="RequestId">
        Unique identifier for the MCP request
      </ResponseField>
    </Expandable>
  </ResponseField>
</Card>

## Basic Example

```python
from fastmcp import Client
from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext

async def basic_sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    # Extract message content
    conversation = []
    for message in messages:
        content = message.content.text if hasattr(message.content, 'text') else str(message.content)
        conversation.append(f"{message.role}: {content}")

    # Use the system prompt if provided
    system_prompt = params.systemPrompt or "You are a helpful assistant."

    # Here you would integrate with your preferred LLM service
    # This is just a placeholder response
    return f"Response based on conversation: {' | '.join(conversation)}"

client = Client(
    "my_mcp_server.py",
    sampling_handler=basic_sampling_handler
)
```


# Tool Operations
Source: https://gofastmcp.com/clients/tools

Discover and execute server-side tools with the FastMCP client.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

Tools are executable functions exposed by MCP servers. The FastMCP client provides methods to discover available tools and execute them with arguments.

## Discovering Tools

Use `list_tools()` to retrieve all tools available on the server:

```python
async with client:
    tools = await client.list_tools()
    # tools -> list[mcp.types.Tool]
    
    for tool in tools:
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        if tool.inputSchema:
            print(f"Parameters: {tool.inputSchema}")
```

## Executing Tools

### Basic Execution

Execute a tool using `call_tool()` with the tool name and arguments:

```python
async with client:
    # Simple tool call
    result = await client.call_tool("add", {"a": 5, "b": 3})
    # result -> CallToolResult with structured and unstructured data
    
    # Access structured data (automatically deserialized)
    print(result.data)  # 8 (int) or {"result": 8} for primitive types
    
    # Access traditional content blocks  
    print(result.content[0].text)  # "8" (TextContent)
```

### Advanced Execution Options

The `call_tool()` method supports additional parameters for timeout control and progress monitoring:

```python
async with client:
    # With timeout (aborts if execution takes longer than 2 seconds)
    result = await client.call_tool(
        "long_running_task", 
        {"param": "value"}, 
        timeout=2.0
    )
    
    # With progress handler (to track execution progress)
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )
```

**Parameters:**

* `name`: The tool name (string)
* `arguments`: Dictionary of arguments to pass to the tool (optional)
* `timeout`: Maximum execution time in seconds (optional, overrides client-level timeout)
* `progress_handler`: Progress callback function (optional, overrides client-level handler)

## Handling Results

<VersionBadge version="2.10.0" />

Tool execution returns a `CallToolResult` object with both structured and traditional content. FastMCP's standout feature is the `.data` property, which doesn't just provide raw JSON but actually hydrates complete Python objects including complex types like datetimes, UUIDs, and custom classes.

### CallToolResult Properties

<Card icon="code" title="CallToolResult Properties">
  <ResponseField name=".data" type="Any">
    **FastMCP exclusive**: Fully hydrated Python objects with complex type support (datetimes, UUIDs, custom classes). Goes beyond JSON to provide complete object reconstruction from output schemas.
  </ResponseField>

  <ResponseField name=".content" type="list[mcp.types.ContentBlock]">
    Standard MCP content blocks (`TextContent`, `ImageContent`, `AudioContent`, etc.) available from all MCP servers.
  </ResponseField>

  <ResponseField name=".structured_content" type="dict[str, Any] | None">
    Standard MCP structured JSON data as sent by the server, available from all MCP servers that support structured outputs.
  </ResponseField>

  <ResponseField name=".is_error" type="bool">
    Boolean indicating if the tool execution failed.
  </ResponseField>
</Card>

### Structured Data Access

FastMCP's `.data` property provides fully hydrated Python objects, not just JSON dictionaries. This includes complex type reconstruction:

```python
from datetime import datetime
from uuid import UUID

async with client:
    result = await client.call_tool("get_weather", {"city": "London"})
    
    # FastMCP reconstructs complete Python objects from the server's output schema
    weather = result.data  # Server-defined WeatherReport object
    print(f"Temperature: {weather.temperature}°C at {weather.timestamp}")
    print(f"Station: {weather.station_id}")
    print(f"Humidity: {weather.humidity}%")
    
    # The timestamp is a real datetime object, not a string!
    assert isinstance(weather.timestamp, datetime)
    assert isinstance(weather.station_id, UUID)
    
    # Compare with raw structured JSON (standard MCP)
    print(f"Raw JSON: {result.structured_content}")
    # {"temperature": 20, "timestamp": "2024-01-15T14:30:00Z", "station_id": "123e4567-..."}
    
    # Traditional content blocks (standard MCP)  
    print(f"Text content: {result.content[0].text}")
```

### Fallback Behavior

For tools without output schemas or when deserialization fails, `.data` will be `None`:

```python
async with client:
    result = await client.call_tool("legacy_tool", {"param": "value"})
    
    if result.data is not None:
        # Structured output available and successfully deserialized
        print(f"Structured: {result.data}")
    else:
        # No structured output or deserialization failed - use content blocks
        for content in result.content:
            if hasattr(content, 'text'):
                print(f"Text result: {content.text}")
            elif hasattr(content, 'data'):
                print(f"Binary data: {len(content.data)} bytes")
```

### Primitive Type Unwrapping

<Tip>
  FastMCP servers automatically wrap non-object results (like `int`, `str`, `bool`) in a `{"result": value}` structure to create valid structured outputs. FastMCP clients understand this convention and automatically unwrap the value in `.data` for convenience, so you get the original primitive value instead of a wrapper object.
</Tip>

```python
async with client:
    result = await client.call_tool("calculate_sum", {"a": 5, "b": 3})
    
    # FastMCP client automatically unwraps for convenience
    print(result.data)  # 8 (int) - the original value
    
    # Raw structured content shows the server-side wrapping
    print(result.structured_content)  # {"result": 8}
    
    # Other MCP clients would need to manually access ["result"]
    # value = result.structured_content["result"]  # Not needed with FastMCP!
```

## Error Handling

### Exception-Based Error Handling

By default, `call_tool()` raises a `ToolError` if the tool execution fails:

```python
from fastmcp.exceptions import ToolError

async with client:
    try:
        result = await client.call_tool("potentially_failing_tool", {"param": "value"})
        print("Tool succeeded:", result.data)
    except ToolError as e:
        print(f"Tool failed: {e}")
```

### Manual Error Checking

You can disable automatic error raising and manually check the result:

```python
async with client:
    result = await client.call_tool(
        "potentially_failing_tool", 
        {"param": "value"}, 
        raise_on_error=False
    )
    
    if result.is_error:
        print(f"Tool failed: {result.content[0].text}")
    else:
        print(f"Tool succeeded: {result.data}")
```

### Raw MCP Protocol Access

For complete control, use `call_tool_mcp()` which returns the raw MCP protocol object:

```python
async with client:
    result = await client.call_tool_mcp("potentially_failing_tool", {"param": "value"})
    # result -> mcp.types.CallToolResult
    
    if result.isError:
        print(f"Tool failed: {result.content}")
    else:
        print(f"Tool succeeded: {result.content}")
        # Note: No automatic deserialization with call_tool_mcp()
```

## Argument Handling

Arguments are passed as a dictionary to the tool:

```python
async with client:
    # Simple arguments
    result = await client.call_tool("greet", {"name": "World"})
    
    # Complex arguments
    result = await client.call_tool("process_data", {
        "config": {"format": "json", "validate": True},
        "items": [1, 2, 3, 4, 5],
        "metadata": {"source": "api", "version": "1.0"}
    })
```

<Tip>
  For multi-server clients, tool names are automatically prefixed with the server name (e.g., `weather_get_forecast` for a tool named `get_forecast` on the `weather` server).
</Tip>


# Client Transports
Source: https://gofastmcp.com/clients/transports

Configure how FastMCP Clients connect to and communicate with servers.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

The FastMCP `Client` communicates with MCP servers through transport objects that handle the underlying connection mechanics. While the client can automatically select a transport based on what you pass to it, instantiating transports explicitly gives you full control over configuration—environment variables, authentication, session management, and more.

Think of transports as configurable adapters between your client code and MCP servers. Each transport type handles a different communication pattern: subprocesses with pipes, HTTP connections, or direct in-memory calls.

## Choosing the Right Transport

* **Use [STDIO Transport](#stdio-transport)** when you need to run local MCP servers with full control over their environment and lifecycle
* **Use [Remote Transports](#remote-transports)** when connecting to production services or shared MCP servers running independently
* **Use [In-Memory Transport](#in-memory-transport)** for testing FastMCP servers without subprocess or network overhead
* **Use [MCP JSON Configuration](#mcp-json-configuration-transport)** when you need to connect to multiple servers defined in configuration files

## STDIO Transport

STDIO (Standard Input/Output) transport communicates with MCP servers through subprocess pipes. This is the standard mechanism used by desktop clients like Claude Desktop and is the primary way to run local MCP servers.

### The Client Runs the Server

<Warning>
  **Critical Concept**: When using STDIO transport, your client actually launches and manages the server process. This is fundamentally different from network transports where you connect to an already-running server. Understanding this relationship is key to using STDIO effectively.
</Warning>

With STDIO transport, your client:

* Starts the server as a subprocess when you connect
* Manages the server's lifecycle (start, stop, restart)
* Controls the server's environment and configuration
* Communicates through stdin/stdout pipes

This architecture enables powerful local integrations but requires understanding environment isolation and process management.

### Environment Isolation

STDIO servers run in isolated environments by default. This is a security feature enforced by the MCP protocol to prevent accidental exposure of sensitive data.

When your client launches an MCP server:

* The server does NOT inherit your shell's environment variables
* API keys, paths, and other configuration must be explicitly passed
* The working directory and system paths may differ from your shell

To pass environment variables to your server, use the `env` parameter:

```python
from fastmcp import Client

# If your server needs environment variables (like API keys),
# you must explicitly pass them:
client = Client(
    "my_server.py",
    env={"API_KEY": "secret", "DEBUG": "true"}
)

# This won't work - the server runs in isolation:
# export API_KEY="secret"  # in your shell
# client = Client("my_server.py")  # server can't see API_KEY
```

### Basic Usage

To use STDIO transport, you create a transport instance with the command and arguments needed to run your server:

```python
from fastmcp.client.transports import StdioTransport

transport = StdioTransport(
    command="python",
    args=["my_server.py"]
)
client = Client(transport)
```

You can configure additional settings like environment variables, working directory, or command arguments:

```python
transport = StdioTransport(
    command="python",
    args=["my_server.py", "--verbose"],
    env={"LOG_LEVEL": "DEBUG"},
    cwd="/path/to/server"
)
client = Client(transport)
```

For convenience, the client can also infer STDIO transport from file paths, but this doesn't allow configuration:

```python
from fastmcp import Client

client = Client("my_server.py")  # Limited - no configuration options
```

### Environment Variables

Since STDIO servers don't inherit your environment, you need strategies for passing configuration. Here are two common approaches:

**Selective forwarding** passes only the variables your server actually needs:

```python
import os
from fastmcp.client.transports import StdioTransport

required_vars = ["API_KEY", "DATABASE_URL", "REDIS_HOST"]
env = {
    var: os.environ[var] 
    for var in required_vars 
    if var in os.environ
}

transport = StdioTransport(
    command="python",
    args=["server.py"],
    env=env
)
client = Client(transport)
```

**Loading from .env files** keeps configuration separate from code:

```python
from dotenv import dotenv_values
from fastmcp.client.transports import StdioTransport

env = dotenv_values(".env")
transport = StdioTransport(
    command="python",
    args=["server.py"],
    env=env
)
client = Client(transport)
```

### Session Persistence

STDIO transports maintain sessions across multiple client contexts by default (`keep_alive=True`). This improves performance by reusing the same subprocess for multiple connections, but can be controlled when you need isolation.

By default, the subprocess persists between connections:

```python
from fastmcp.client.transports import StdioTransport

transport = StdioTransport(
    command="python",
    args=["server.py"]
)
client = Client(transport)

async def efficient_multiple_operations():
    async with client:
        await client.ping()
    
    async with client:  # Reuses the same subprocess
        await client.call_tool("process_data", {"file": "data.csv"})
```

For complete isolation between connections, disable session persistence:

```python
transport = StdioTransport(
    command="python",
    args=["server.py"],
    keep_alive=False
)
client = Client(transport)
```

Use `keep_alive=False` when you need complete isolation (e.g., in test suites) or when server state could cause issues between connections.

### Specialized STDIO Transports

FastMCP provides convenience transports that are thin wrappers around `StdioTransport` with pre-configured commands:

* **`PythonStdioTransport`** - Uses `python` command for `.py` files
* **`NodeStdioTransport`** - Uses `node` command for `.js` files
* **`UvxStdioTransport`** - Uses `uvx` for Python packages (uses `env_vars` parameter)
* **`NpxStdioTransport`** - Uses `npx` for Node packages (uses `env_vars` parameter)

For most use cases, instantiate `StdioTransport` directly with your desired command. These specialized transports are primarily useful for client inference shortcuts.

## Remote Transports

Remote transports connect to MCP servers running as web services. This is a fundamentally different model from STDIO transports—instead of your client launching and managing a server process, you connect to an already-running service that manages its own environment and lifecycle.

### Streamable HTTP Transport

<VersionBadge version="2.3.0" />

Streamable HTTP is the recommended transport for production deployments, providing efficient bidirectional streaming over HTTP connections.

* **Class:** `StreamableHttpTransport`
* **Server compatibility:** FastMCP servers running with `mcp run --transport http`

The transport requires a URL and optionally supports custom headers for authentication and configuration:

```python
from fastmcp.client.transports import StreamableHttpTransport

# Basic connection
transport = StreamableHttpTransport(url="https://api.example.com/mcp")
client = Client(transport)

# With custom headers for authentication
transport = StreamableHttpTransport(
    url="https://api.example.com/mcp",
    headers={
        "Authorization": "Bearer your-token-here",
        "X-Custom-Header": "value"
    }
)
client = Client(transport)
```

For convenience, FastMCP also provides authentication helpers:

```python
from fastmcp.client.auth import BearerAuth

client = Client(
    "https://api.example.com/mcp",
    auth=BearerAuth("your-token-here")
)
```

### SSE Transport (Legacy)

Server-Sent Events transport is maintained for backward compatibility but is superseded by Streamable HTTP for new deployments.

* **Class:** `SSETransport`
* **Server compatibility:** FastMCP servers running with `mcp run --transport sse`

SSE transport supports the same configuration options as Streamable HTTP:

```python
from fastmcp.client.transports import SSETransport

transport = SSETransport(
    url="https://api.example.com/sse",
    headers={"Authorization": "Bearer token"}
)
client = Client(transport)
```

Use Streamable HTTP for new deployments unless you have specific infrastructure requirements for SSE.

## In-Memory Transport

In-memory transport connects directly to a FastMCP server instance within the same Python process. This eliminates both subprocess management and network overhead, making it ideal for testing and development.

* **Class:** `FastMCPTransport`

<Note>
  Unlike STDIO transports, in-memory servers have full access to your Python process's environment. They share the same memory space and environment variables as your client code—no isolation or explicit environment passing required.
</Note>

```python
from fastmcp import FastMCP, Client
import os

mcp = FastMCP("TestServer")

@mcp.tool
def greet(name: str) -> str:
    prefix = os.environ.get("GREETING_PREFIX", "Hello")
    return f"{prefix}, {name}!"

client = Client(mcp)

async with client:
    result = await client.call_tool("greet", {"name": "World"})
```

## MCP JSON Configuration Transport

<VersionBadge version="2.4.0" />

This transport supports the emerging MCP JSON configuration standard for defining multiple servers:

* **Class:** `MCPConfigTransport`

```python
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http"
        },
        "assistant": {
            "command": "python",
            "args": ["./assistant.py"],
            "env": {"LOG_LEVEL": "INFO"}
        }
    }
}

client = Client(config)

async with client:
    # Tools are namespaced by server
    weather = await client.call_tool("weather_get_forecast", {"city": "NYC"})
    answer = await client.call_tool("assistant_ask", {"question": "What?"})
```

### Tool Transformation with FastMCP and MCPConfig

FastMCP supports basic tool transformations to be defined alongside the MCP Servers in the MCPConfig file.

```python
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http",
            "tools": { }   #  <--- This is the tool transformation section
        }
    }
}
```

With these transformations, you can transform (change) the name, title, description, tags, enablement, and arguments of a tool.

For each argument the tool takes, you can transform (change) the name, description, default, visibility, whether it's required, and you can provide example values.

In the following example, we're transforming the `weather_get_forecast` tool to only retrieve the weather for `Miami` and hiding the `city` argument from the client.

```python
tool_transformations = {
    "weather_get_forecast": {
        "name": "miami_weather",
        "description": "Get the weather for Miami",
        "arguments": {
            "city": {
                "name": "city",
                "default": "Miami",
                "hide": True,
            }
        }
    }
}

config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http",
            "tools": tool_transformations
        }
    }
}
```

#### Allowlisting and Blocklisting Tools

Tools can be allowlisted or blocklisted from the client by applying `tags` to the tools on the server. In the following example, we're allowlisting only tools marked with the `forecast` tag, all other tools will be unavailable to the client.

```python
tool_transformations = {
    "weather_get_forecast": {
        "enabled": True,
        "tags": ["forecast"]
    }
}


config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http",
            "tools": tool_transformations,
            "include_tags": ["forecast"]
        }
    }
}
```


# Community Showcase
Source: https://gofastmcp.com/community/showcase

High-quality projects and examples from the FastMCP community

export const YouTubeEmbed = ({videoId, title}) => {
  return <iframe className="w-full aspect-video rounded-md" src={`https://www.youtube.com/embed/${videoId}`} title={title} frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />;
};

## Featured Projects

Discover exemplary MCP servers and implementations created by our community. These projects demonstrate best practices and innovative uses of FastMCP.

### Learning Resources

<Card title="MCP Dummy Server" icon="graduation-cap" href="https://github.com/WaiYanNyeinNaing/mcp-dummy-server">
  A comprehensive educational example demonstrating FastMCP best practices with professional dual-transport server implementation, interactive test client, and detailed documentation.
</Card>

#### Video Tutorials

**Build Remote MCP Servers w/ Python & FastMCP** - Claude Integrations Tutorial by Greg + Code

<YouTubeEmbed videoId="bOYkbXP-GGo" title="Build Remote MCP Servers w/ Python & FastMCP" />

**FastMCP — the best way to build an MCP server with Python** - Tutorial by ZazenCodes

<YouTubeEmbed videoId="rnljvmHorQw" title="FastMCP — the best way to build an MCP server with Python" />

**Speedrun a MCP server for Claude Desktop (fastmcp)** - Tutorial by Nate from Prefect

<YouTubeEmbed videoId="67ZwpkUEtSI" title="Speedrun a MCP server for Claude Desktop (fastmcp)" />

### Community Examples

Have you built something interesting with FastMCP? We'd love to feature high-quality examples here! Start a [discussion on GitHub](https://github.com/jlowin/fastmcp/discussions) to share your project.

## Contributing

To get your project featured:

1. Ensure your project demonstrates best practices
2. Include comprehensive documentation
3. Add clear usage examples
4. Open a discussion in our [GitHub Discussions](https://github.com/jlowin/fastmcp/discussions)

We review submissions regularly and feature projects that provide value to the FastMCP community.

## Further Reading

* [Contrib Modules](/patterns/contrib) - Community-contributed modules that are distributed with FastMCP itself


# Running Your FastMCP Server
Source: https://gofastmcp.com/deployment/running-server

Learn how to run and deploy your FastMCP server using various transport protocols like STDIO, Streamable HTTP, and SSE.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

FastMCP servers can be run in different ways depending on your application's needs, from local command-line tools to persistent web services. This guide covers the primary methods for running your server, focusing on the available transport protocols: STDIO, Streamable HTTP, and SSE.

## The `run()` Method

FastMCP servers can be run directly from Python by calling the `run()` method on a `FastMCP` instance.

<Tip>
  For maximum compatibility, it's best practice to place the `run()` call within an `if __name__ == "__main__":` block. This ensures the server starts only when the script is executed directly, not when imported as a module.
</Tip>

```python {9-10} my_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

You can now run this MCP server by executing `python my_server.py`.

MCP servers can be run with a variety of different transport options, depending on your application's requirements. The `run()` method can take a `transport` argument and other transport-specific keyword arguments to configure how the server operates.

## The FastMCP CLI

FastMCP also provides a command-line interface for running servers without modifying the source code. After installing FastMCP, you can run your server directly from the command line:

```bash
fastmcp run server.py
```

<Tip>
  **Important**: When using `fastmcp run`, it **ignores** the `if __name__ == "__main__"` block entirely. Instead, it looks for a FastMCP object named `mcp`, `server`, or `app` and calls its `run()` method directly with the transport options you specify.

  This means you can use `fastmcp run` to override the transport specified in your code, which is particularly useful for testing or changing deployment methods without modifying the code.
</Tip>

You can specify transport options and other configuration:

```bash
fastmcp run server.py --transport sse --port 9000
```

### Dependency Management with CLI

When using the FastMCP CLI, you can pass additional options to configure how `uv` runs your server:

```bash
# Run with a specific Python version
fastmcp run server.py --python 3.11

# Run with additional packages
fastmcp run server.py --with pandas --with numpy

# Run with dependencies from a requirements file
fastmcp run server.py --with-requirements requirements.txt

# Combine multiple options
fastmcp run server.py --python 3.10 --with httpx --transport http

# Run within a specific project directory
fastmcp run server.py --project /path/to/project
```

<Note>
  When using `--python`, `--with`, `--project`, or `--with-requirements`, the server runs via `uv run` subprocess instead of using your local environment. The `uv` command will manage dependencies based on your project configuration.
</Note>

<Tip>
  The `--python` option is particularly useful when you need to run a server with a specific Python version that differs from your system's default. This addresses common compatibility issues where servers require a particular Python version to function correctly.
</Tip>

For development and testing, you can use the `dev` command to run your server with the MCP Inspector:

```bash
fastmcp dev server.py
```

The `dev` command also supports the same dependency management options:

```bash
# Dev server with specific Python version and packages
fastmcp dev server.py --python 3.11 --with pandas
```

See the [CLI documentation](/patterns/cli) for detailed information about all available commands and options.

### Passing Arguments to Servers

When servers accept command line arguments (using argparse, click, or other libraries), you can pass them after `--`:

```bash
fastmcp run config_server.py -- --config config.json
fastmcp run database_server.py -- --database-path /tmp/db.sqlite --debug
```

This is useful for servers that need configuration files, database paths, API keys, or other runtime options.

## Transport Options

Below is a comparison of available transport options to help you choose the right one for your needs:

| Transport           | Use Cases                                                                            | Recommendation                                                |
| ------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **STDIO**           | Local tools, command-line scripts, and integrations with clients like Claude Desktop | Best for local tools and when clients manage server processes |
| **Streamable HTTP** | Web-based deployments, microservices, exposing MCP over a network                    | Recommended choice for web-based deployments                  |
| **SSE**             | Existing web-based deployments that rely on SSE                                      | Deprecated - prefer Streamable HTTP for new projects          |

### STDIO

The STDIO transport is the default and most widely compatible option for local MCP server execution. It is ideal for local tools, command-line integrations, and clients like Claude Desktop. However, it has the disadvantage of having to run the MCP code locally, which can introduce security concerns with third-party servers.

STDIO is the default transport, so you don't need to specify it when calling `run()`. However, you can specify it explicitly to make your intent clear:

```python {6}
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

When using Stdio transport, you will typically *not* run the server yourself as a separate process. Rather, your *clients* will spin up a new server process for each session. As such, no additional configuration is required.

### Streamable HTTP

<VersionBadge version="2.3.0" />

Streamable HTTP is a modern, efficient transport for exposing your MCP server via HTTP. It is the recommended transport for web-based deployments.

To run a server using Streamable HTTP, you can use the `run()` method with the `transport` argument set to `"http"`. This will start a Uvicorn server on the default host (`127.0.0.1`), port (`8000`), and path (`/mcp/`).

<CodeGroup>
  ```python {6} server.py
  from fastmcp import FastMCP

  mcp = FastMCP()

  if __name__ == "__main__":
      mcp.run(transport="http")
  ```

  ```python {5} client.py
  import asyncio
  from fastmcp import Client

  async def example():
      async with Client("http://127.0.0.1:8000/mcp/") as client:
          await client.ping()

  if __name__ == "__main__":
      asyncio.run(example())
  ```
</CodeGroup>

<Tip>
  For backward compatibility, wherever `"http"` is accepted as a transport name, you can also pass `"streamable-http"` as a fully supported alias. This is particularly useful when upgrading from FastMCP 1.x in the official Python SDK and FastMCP \<= 2.9, where `"streamable-http"` was the standard name.
</Tip>

To customize the host, port, path, or log level, provide appropriate keyword arguments to the `run()` method.

<CodeGroup>
  ```python {8-11} server.py
  from fastmcp import FastMCP

  mcp = FastMCP()

  if __name__ == "__main__":
      mcp.run(
          transport="http",
          host="127.0.0.1",
          port=4200,
          path="/my-custom-path",
          log_level="debug",
      )
  ```

  ```python {5} client.py
  import asyncio
  from fastmcp import Client

  async def example():
      async with Client("http://127.0.0.1:4200/my-custom-path") as client:
          await client.ping()

  if __name__ == "__main__":
      asyncio.run(example())
  ```
</CodeGroup>

### SSE

<Warning>
  The SSE transport is deprecated and may be removed in a future version.
  New applications should use Streamable HTTP transport instead.
</Warning>

Server-Sent Events (SSE) is an HTTP-based protocol for server-to-client streaming. While FastMCP still supports SSE, it is deprecated and Streamable HTTP is preferred for new projects.

To run a server using SSE, you can use the `run()` method with the `transport` argument set to `"sse"`. This will start a Uvicorn server on the default host (`127.0.0.1`), port (`8000`), and with default SSE path (`/sse/`) and message path (`/messages/`).

<CodeGroup>
  ```python {6} server.py
  from fastmcp import FastMCP

  mcp = FastMCP()

  if __name__ == "__main__":
      mcp.run(transport="sse")
  ```

  ```python {3,7} client.py
  import asyncio
  from fastmcp import Client
  from fastmcp.client.transports import SSETransport

  async def example():
      async with Client(
          transport=SSETransport("http://127.0.0.1:8000/sse/")
      ) as client:
          await client.ping()

  if __name__ == "__main__":
      asyncio.run(example())
  ```
</CodeGroup>

<Tip>
  Notice that the client in the above example uses an explicit `SSETransport` to connect to the server. FastMCP will attempt to infer the appropriate transport from the provided configuration, but HTTP URLs are assumed to be Streamable HTTP (as of FastMCP 2.3.0).
</Tip>

To customize the host, port, or log level, provide appropriate keyword arguments to the `run()` method. You can also adjust the SSE path (which clients should connect to) and the message POST endpoint (which clients use to send subsequent messages).

<CodeGroup>
  ```python {8-12} server.py
  from fastmcp import FastMCP

  mcp = FastMCP()

  if __name__ == "__main__":
      mcp.run(
          transport="sse",
          host="127.0.0.1",
          port=4200,
          log_level="debug",
          path="/my-custom-sse-path",
      )
  ```

  ```python {7} client.py
  import asyncio
  from fastmcp import Client
  from fastmcp.client.transports import SSETransport

  async def example():
      async with Client(
          transport=SSETransport("http://127.0.0.1:4200/my-custom-sse-path")
      ) as client:
          await client.ping()

  if __name__ == "__main__":
      asyncio.run(example())
  ```
</CodeGroup>

## Async Usage

FastMCP provides both synchronous and asynchronous APIs for running your server. The `run()` method seen in previous examples is a synchronous method that internally uses `anyio.run()` to run the asynchronous server. For applications that are already running in an async context, FastMCP provides the `run_async()` method.

```python {10-12}
from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="http")

if __name__ == "__main__":
    asyncio.run(main())
```

<Warning>
  The `run()` method cannot be called from inside an async function because it already creates its own async event loop internally. If you attempt to call `run()` from inside an async function, you'll get an error about the event loop already running.

  Always use `run_async()` inside async functions and `run()` in synchronous contexts.
</Warning>

Both `run()` and `run_async()` accept the same transport arguments, so all the examples above apply to both methods.

## Custom Routes

You can also add custom web routes to your FastMCP server, which will be exposed alongside the MCP endpoint. To do so, use the `@custom_route` decorator. Note that this is less flexible than using a full ASGI framework, but can be useful for adding simple endpoints like health checks to your standalone server.

```python
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run()
```


# Installation
Source: https://gofastmcp.com/getting-started/installation



## Install FastMCP

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install and manage FastMCP.

If you plan to use FastMCP in your project, you can add it as a dependency with:

```bash
uv add fastmcp
```

Alternatively, you can install it directly with `pip` or `uv pip`:

<CodeGroup>
  ```bash uv
  uv pip install fastmcp
  ```

  ```bash pip
  pip install fastmcp
  ```
</CodeGroup>

### Verify Installation

To verify that FastMCP is installed correctly, you can run the following command:

```bash
fastmcp version
```

You should see output like the following:

```bash
$ fastmcp version

FastMCP version:   0.4.2.dev41+ga077727.d20250410
MCP version:                                1.6.0
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp
```

## Upgrading from the Official MCP SDK

Upgrading from the official MCP SDK's FastMCP 1.0 to FastMCP 2.0 is generally straightforward. The core server API is highly compatible, and in many cases, changing your import statement from `from mcp.server.fastmcp import FastMCP` to `from fastmcp import FastMCP` will be sufficient.

```python {5}
# Before
# from mcp.server.fastmcp import FastMCP

# After
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```

<Warning>
  Prior to `fastmcp==2.3.0` and `mcp==1.8.0`, the 2.x API always mirrored the official 1.0 API. However, as the projects diverge, this can not be guaranteed. You may see deprecation warnings if you attempt to use 1.0 APIs in FastMCP 2.x. Please refer to this documentation for details on new capabilities.
</Warning>

## Versioning and Breaking Changes

While we make every effort not to introduce backwards-incompatible changes to our public APIs and behavior, FastMCP exists in a rapidly evolving MCP landscape. We're committed to bringing the most cutting-edge features to our users, which occasionally necessitates changes to existing functionality.

As a practice, breaking changes will only occur on minor version changes (e.g., 2.3.x to 2.4.0). A minor version change indicates either:

* A significant new feature set that warrants a new minor version
* Introducing breaking changes that may affect behavior on upgrade

For users concerned about stability in production environments, we recommend pinning FastMCP to a specific version in your dependencies.

Whenever possible, FastMCP will issue deprecation warnings when users attempt to use APIs that are either deprecated or destined for future removal. These warnings will be maintained for at least 1 minor version release, and may be maintained longer.

Note that the "public API" includes the public functionality of the `FastMCP` server, core FastMCP components like `Tool`, `Prompt`, `Resource`, and `ResourceTemplate`, and their respective public methods. It does not include private methods, utilities, or objects that are stored as private attributes, as we do not expect users to rely on those implementation details.

## Installing for Development

If you plan to contribute to FastMCP, you should begin by cloning the repository and using uv to install all dependencies (development dependencies are installed automatically):

```bash
git clone https://github.com/jlowin/fastmcp.git
cd fastmcp
uv sync
```

This will install all dependencies, including ones for development, and create a virtual environment, which you can activate and use as normal.

### Unit Tests

FastMCP has a comprehensive unit test suite, and all PR's must introduce and pass appropriate tests. To run the tests, use pytest:

```bash
pytest
```

### Pre-Commit Hooks

FastMCP uses pre-commit to manage code quality, including formatting, linting, and type-safety. All PRs must pass the pre-commit hooks, which are run as a part of the CI process. To install the pre-commit hooks, run:

```bash
uv run pre-commit install
```

Alternatively, to run pre-commit manually at any time, use:

```bash
pre-commit run --all-files
```


# Quickstart
Source: https://gofastmcp.com/getting-started/quickstart



Welcome! This guide will help you quickly set up FastMCP and run your first MCP server.

If you haven't already installed FastMCP, follow the [installation instructions](/getting-started/installation).

## Creating a FastMCP Server

A FastMCP server is a collection of tools, resources, and other MCP components. To create a server, start by instantiating the `FastMCP` class.

Create a new file called `my_server.py` and add the following code:

```python my_server.py
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```

That's it! You've created a FastMCP server, albeit a very boring one. Let's add a tool to make it more interesting.

## Adding a Tool

To add a tool that returns a simple greeting, write a function and decorate it with `@mcp.tool` to register it with the server:

```python my_server.py {5-7}
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## Testing the Server

To test the server, create a FastMCP client and point it at the server object.

```python my_server.py {1-2, 10-17}
import asyncio
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

client = Client(mcp)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))
```

There are a few things to note here:

* Clients are asynchronous, so we need to use `asyncio.run` to run the client.
* We must enter a client context (`async with client:`) before using the client. You can make multiple client calls within the same context.

## Running the server

In order to run the server with Python, we need to add a `run` statement to the `__main__` block of the server file.

```python my_server.py {9-10}
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

This lets us run the server with `python my_server.py`, using the default `stdio` transport, which is the standard way to expose an MCP server to a client.

<Tip>
  Why do we need the `if __name__ == "__main__":` block?

  Within the FastMCP ecosystem, this line may be unnecessary. However, including it ensures that your FastMCP server runs for all users and clients in a consistent way and is therefore recommended as best practice.
</Tip>

### Interacting with the Python server

Now that the server can be executed with `python my_server.py`, we can interact with it like any other MCP server.

In a new file, create a client and point it at the server file:

```python my_client.py
import asyncio
from fastmcp import Client

client = Client("my_server.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))
```

### Using the FastMCP CLI

To have FastMCP run the server for us, we can use the `fastmcp run` command. This will start the server and keep it running until it is stopped. By default, it will use the `stdio` transport, which is a simple text-based protocol for interacting with the server.

```bash
fastmcp run my_server.py:mcp
```

Note that FastMCP *does not* require the `__main__` block in the server file, and will ignore it if it is present. Instead, it looks for the server object provided in the CLI command (here, `mcp`). If no server object is provided, `fastmcp run` will automatically search for servers called "mcp", "app", or "server" in the file.

<Tip>
  We pointed our client at the server file, which is recognized as a Python MCP server and executed with `python my_server.py` by default. This executes the `__main__` block of the server file. There are other ways to run the server, which are described in the [server configuration](/servers/server#running-the-server) guide.
</Tip>


# Welcome to FastMCP 2.0!
Source: https://gofastmcp.com/getting-started/welcome

The fast, Pythonic way to build MCP servers and clients.

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is a new, standardized way to provide context and tools to your LLMs, and FastMCP makes building MCP servers and clients simple and intuitive. Create tools, expose resources, define prompts, and more with clean, Pythonic code:

```python {1}
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## Beyond the Protocol

FastMCP is the standard framework for working with the Model Context Protocol. FastMCP 1.0 was incorporated into the [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) in 2024.

This is FastMCP 2.0, the **actively maintained version** that provides a complete toolkit for working with the MCP ecosystem.

FastMCP 2.0 has a comprehensive set of features that go far beyond the core MCP specification, all in service of providing **the simplest path to production**. These include deployment, auth, clients, server proxying and composition, generating servers from REST APIs, dynamic tool rewriting, built-in testing tools, integrations, and more.

Ready to upgrade or get started? Follow the [installation instructions](/getting-started/installation), which include steps for upgrading from the official MCP SDK.

## What is MCP?

The Model Context Protocol lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as "the USB-C port for AI", providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:

* Expose data through `Resources` (think of these sort of like GET endpoints; they are used to load information into the LLM's context)
* Provide functionality through `Tools` (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
* Define interaction patterns through `Prompts` (reusable templates for LLM interactions)
* And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.

## Why FastMCP?

The MCP protocol is powerful but implementing it involves a lot of boilerplate - server setup, protocol handlers, content types, error management. FastMCP handles all the complex protocol details and server management, so you can focus on building great tools. It's designed to be high-level and Pythonic; in most cases, decorating a function is all you need.

FastMCP 2.0 has evolved into a comprehensive platform that goes far beyond basic protocol implementation. While 1.0 provided server-building capabilities (and is now part of the official MCP SDK), 2.0 offers a complete ecosystem including client libraries, authentication systems, deployment tools, integrations with major AI platforms, testing frameworks, and production-ready infrastructure patterns.

FastMCP aims to be:

🚀 **Fast**: High-level interface means less code and faster development

🍀 **Simple**: Build MCP servers with minimal boilerplate

🐍 **Pythonic**: Feels natural to Python developers

🔍 **Complete**: A comprehensive platform for all MCP use cases, from dev to prod

FastMCP is made with 💙 by [Prefect](https://www.prefect.io/).

## LLM-Friendly Docs

This documentation is also available in [llms.txt format](https://llmstxt.org/), which is a simple markdown standard that LLMs can consume easily.

There are two ways to access the LLM-friendly documentation:

* [llms.txt](https://gofastmcp.com/llms.txt) is essentially a sitemap, listing all the pages in the documentation.
* [llms-full.txt](https://gofastmcp.com/llms-full.txt) contains the entire documentation. Note this may exceed the context window of your LLM.

In addition, any page can be accessed as markdown by appending `.md` to the URL. For example, this page would become `https://gofastmcp.com/getting-started/welcome.md`, which you can view [here](/getting-started/welcome.md).

Finally, you can copy the contents of any page as markdown by pressing "Cmd+C" (or "Ctrl+C" on Windows) on your keyboard.


# Anthropic API 🤝 FastMCP
Source: https://gofastmcp.com/integrations/anthropic

Call FastMCP servers from the Anthropic API

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

Anthropic's [Messages API](https://docs.anthropic.com/en/api/messages) supports MCP servers as remote tool sources. This tutorial will show you how to create a FastMCP server and deploy it to a public URL, then how to call it from the Messages API.

<Tip>
  Currently, the MCP connector only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to Claude. Other MCP features like resources and prompts are not currently supported. You can read more about the MCP connector in the [Anthropic documentation](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector).
</Tip>

## Create a Server

First, create a FastMCP server with the tools you want to expose. For this example, we'll create a server with a single tool that rolls dice.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
```

## Deploy the Server

Your server must be deployed to a public URL in order for Anthropic to access it. The MCP connector supports both SSE and Streamable HTTP transports.

For development, you can use tools like `ngrok` to temporarily expose a locally-running server to the internet. We'll do that for this example (you may need to install `ngrok` and create a free account), but you can use any other method to deploy your server.

Assuming you saved the above code as `server.py`, you can run the following two commands in two separate terminals to deploy your server and expose it to the internet:

<CodeGroup>
  ```bash FastMCP server
  python server.py
  ```

  ```bash ngrok
  ngrok http 8000
  ```
</CodeGroup>

<Warning>
  This exposes your unauthenticated server to the internet. Only run this command in a safe environment if you understand the risks.
</Warning>

## Call the Server

To use the Messages API with MCP servers, you'll need to install the Anthropic Python SDK (not included with FastMCP):

```bash
pip install anthropic
```

You'll also need to authenticate with Anthropic. You can do this by setting the `ANTHROPIC_API_KEY` environment variable. Consult the Anthropic SDK documentation for more information.

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

Here is an example of how to call your server from Python. Note that you'll need to replace `https://your-server-url.com` with the actual URL of your server. In addition, we use `/mcp/` as the endpoint because we deployed a streamable-HTTP server with the default path; you may need to use a different endpoint if you customized your server's deployment. **At this time you must also include the `extra_headers` parameter with the `anthropic-beta` header.**

```python {5, 13-22}
import anthropic
from rich import print

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Roll a few dice!"}],
    mcp_servers=[
        {
            "type": "url",
            "url": f"{url}/mcp/",
            "name": "dice-server",
        }
    ],
    extra_headers={
        "anthropic-beta": "mcp-client-2025-04-04"
    }
)

print(response.content)
```

If you run this code, you'll see something like the following output:

```text
I'll roll some dice for you! Let me use the dice rolling tool.

I rolled 3 dice and got: 4, 2, 6

The results were 4, 2, and 6. Would you like me to roll again or roll a different number of dice?
```

## Authentication

<VersionBadge version="2.6.0" />

The MCP connector supports OAuth authentication through authorization tokens, which means you can secure your server while still allowing Anthropic to access it.

### Server Authentication

The simplest way to add authentication to the server is to use a bearer token scheme.

For this example, we'll quickly generate our own tokens with FastMCP's `RSAKeyPair` utility, but this may not be appropriate for production use. For more details, see the complete server-side [Bearer Auth](/servers/auth/bearer) documentation.

We'll start by creating an RSA key pair to sign and verify tokens.

```python
from fastmcp.server.auth.providers.bearer import RSAKeyPair

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")
```

<Warning>
  FastMCP's `RSAKeyPair` utility is for development and testing only.
</Warning>

Next, we'll create a `BearerAuthProvider` to authenticate the server.

```python
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)
```

Here is a complete example that you can copy/paste. For simplicity and the purposes of this example only, it will print the token to the console. **Do NOT do this in production!**

```python server.py [expandable]
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair
import random

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    print(f"\n---\n\n🔑 Dice Roller access token:\n\n{access_token}\n\n---\n")
    mcp.run(transport="http", port=8000)
```

### Client Authentication

If you try to call the authenticated server with the same Anthropic code we wrote earlier, you'll get an error indicating that the server rejected the request because it's not authenticated.

```python
Error code: 400 - {
    "type": "error", 
    "error": {
        "type": "invalid_request_error", 
        "message": "MCP server 'dice-server' requires authentication. Please provide an authorization_token.",
    },
}
```

To authenticate the client, you can pass the token using the `authorization_token` parameter in your MCP server configuration:

```python {8, 21}
import anthropic
from rich import print

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

# Your access token (replace with your actual token)
access_token = 'your-access-token'

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Roll a few dice!"}],
    mcp_servers=[
        {
            "type": "url",
            "url": f"{url}/mcp/",
            "name": "dice-server",
            "authorization_token": access_token
        }
    ],
    extra_headers={
        "anthropic-beta": "mcp-client-2025-04-04"
    }
)

print(response.content)
```

You should now see the dice roll results in the output.


# ChatGPT 🤝 FastMCP
Source: https://gofastmcp.com/integrations/chatgpt

Connect FastMCP servers to ChatGPT Deep Research

ChatGPT supports MCP servers through remote HTTP connections, allowing you to extend ChatGPT's capabilities with custom tools and knowledge from your FastMCP servers.

<Note>
  MCP integration with ChatGPT is currently limited to **Deep Research** functionality and is not available for general chat. This feature is available for ChatGPT Pro, Team, Enterprise, and Edu users.
</Note>

<Tip>
  OpenAI's official MCP documentation and examples are built with **FastMCP v2**! Check out their [simple Deep Research-style MCP server example](https://github.com/openai/sample-deep-research-mcp) for a quick reference similar to the one in this document, or their [more complete Deep Research example](https://github.com/openai/openai-cookbook/tree/main/examples/deep_research_api/how_to_build_a_deep_research_mcp_server) from the OpenAI Cookbook, which includes vector search and more.
</Tip>

## Deep Research

ChatGPT's Deep Research feature requires MCP servers to be internet-accessible HTTP endpoints with **exactly two specific tools**:

* **`search`**: For searching through your resources and returning matching IDs
* **`fetch`**: For retrieving the full content of specific resources by ID

<Warning>
  If your server doesn't implement both `search` and `fetch` tools with the correct signatures, ChatGPT will show the error: "This MCP server doesn't implement our specification". Both tools are required.
</Warning>

### Tool Descriptions Matter

Since ChatGPT needs to understand how to use your tools effectively, **write detailed tool descriptions**. The description teaches ChatGPT how to form queries, what parameters to use, and what to expect from your data. Poor descriptions lead to poor search results.

### Create a Server

A Deep Research-compatible server must implement these two required tools:

* **`search(query: str)`** - Takes a query of any kind and returns matching record IDs
* **`fetch(id: str)`** - Takes an ID and returns the record

**Critical**: Write detailed docstrings for both tools. These descriptions teach ChatGPT how to use your tools effectively. Poor descriptions lead to poor search results.

The `search` tool should take a query (of any kind!) and return IDs. The `fetch` tool should take an ID and return the record.

Here's a reference server implementation you can adapt (see also [OpenAI's sample server](https://github.com/openai/sample-deep-research-mcp) for comparison):

```python server.py [expandable]
import json
from pathlib import Path
from dataclasses import dataclass
from fastmcp import FastMCP

@dataclass
class Record:
    id: str
    title: str
    text: str
    metadata: dict

def create_server(
    records_path: Path | str,
    name: str | None = None,
    instructions: str | None = None,
) -> FastMCP:
    """Create a FastMCP server that can search and fetch records from a JSON file."""
    records = json.loads(Path(records_path).read_text())

    RECORDS = [Record(**r) for r in records]
    LOOKUP = {r.id: r for r in RECORDS}

    mcp = FastMCP(name=name or "Deep Research MCP", instructions=instructions)

    @mcp.tool()
    async def search(query: str):
        """
        Simple unranked keyword search across title, text, and metadata.
        Searches for any of the query terms in the record content.
        Returns a list of matching record IDs for ChatGPT to fetch.
        """
        toks = query.lower().split()
        ids = []
        for r in RECORDS:
            record_txt = " ".join(
                [r.title, r.text, " ".join(r.metadata.values())]
            ).lower()
            if any(t in record_txt for t in toks):
                ids.append(r.id)

        return {"ids": ids}

    @mcp.tool()
    async def fetch(id: str):
        """
        Fetch a record by ID.
        Returns the complete record data for ChatGPT to analyze and cite.
        """
        if id not in LOOKUP:
            raise ValueError(f"Unknown record ID: {id}")
        return LOOKUP[id]

    return mcp

if __name__ == "__main__":
    mcp = create_server("path/to/records.json")
    mcp.run(transport="http", port=8000)
```

### Deploy the Server

Your server must be deployed to a public URL in order for ChatGPT to access it.

For development, you can use tools like `ngrok` to temporarily expose a locally-running server to the internet. We'll do that for this example (you may need to install `ngrok` and create a free account), but you can use any other method to deploy your server.

Assuming you saved the above code as `server.py`, you can run the following two commands in two separate terminals to deploy your server and expose it to the internet:

<CodeGroup>
  ```bash FastMCP server
  python server.py
  ```

  ```bash ngrok
  ngrok http 8000
  ```
</CodeGroup>

<Warning>
  This exposes your unauthenticated server to the internet. Only run this command in a safe environment if you understand the risks.
</Warning>

### Connect to ChatGPT

Replace `https://your-server-url.com` with the actual URL of your server (such as your ngrok URL).

1. Open ChatGPT and go to **Settings** → **Connectors**
2. Click **Add custom connector**
3. Enter your server details:
   * **Name**: Library Catalog
   * **URL**: Your server URL, including the path.
     * **Note**: Ensure your URL includes the correct path for the transport you’re using. The defaults are /sse/ for SSE (e.g., [https://abc123.ngrok.io/sse/](https://abc123.ngrok.io/sse/)) and /mcp/ for HTTP (e.g., [https://abc123.ngrok.io/mcp/](https://abc123.ngrok.io/mcp/)).
   * **Description**: A library catalog for searching and retrieving books

#### Test the Connection

1. Start a new chat in ChatGPT
2. Click **Tools** → **Run deep research**
3. Select your **Library Catalog** connector as a source
4. Ask questions like:
   * "Search for Python programming books"
   * "Find books about AI and machine learning"
   * "Show me books by the Python Software Foundation"

ChatGPT will use your server's search and fetch tools to find relevant information and cite the sources in its response.

### Troubleshooting

#### "This MCP server doesn't implement our specification"

If you get this error, it most likely means that your server doesn't implement the required tools (`search` and `fetch`). To correct it, ensure that your server meets the service requirements.


# Claude Code 🤝 FastMCP
Source: https://gofastmcp.com/integrations/claude-code

Install and use FastMCP servers in Claude Code

export const LocalFocusTip = () => {
  return <Tip>
            <strong>This integration focuses on running local FastMCP server files with STDIO transport.</strong> For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and <code>uv</code> commands.
        </Tip>;
};

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<LocalFocusTip />

Claude Code supports MCP servers through multiple transport methods including STDIO, SSE, and HTTP, allowing you to extend Claude's capabilities with custom tools, resources, and prompts from your FastMCP servers.

## Requirements

This integration uses STDIO transport to run your FastMCP server locally. For remote deployments, you can run your FastMCP server with HTTP or SSE transport and configure it directly using Claude Code's built-in MCP management commands.

## Create a Server

The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run()
```

## Install the Server

### FastMCP CLI

<VersionBadge version="2.10.3" />

The easiest way to install a FastMCP server in Claude Code is using the `fastmcp install claude-code` command. This automatically handles the configuration, dependency management, and calls Claude Code's built-in MCP management system.

```bash
fastmcp install claude-code server.py
```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:

```bash
# These are equivalent if your server object is named 'mcp'
fastmcp install claude-code server.py
fastmcp install claude-code server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install claude-code server.py:my_custom_server
```

The command will automatically configure the server with Claude Code's `claude mcp add` command.

#### Dependencies

FastMCP provides flexible dependency management options for your Claude Code servers:

**Individual packages**: Use the `--with` flag to specify packages your server needs. You can use this flag multiple times:

```bash
fastmcp install claude-code server.py --with pandas --with requests
```

**Requirements file**: If you maintain a `requirements.txt` file with all your dependencies, use `--with-requirements` to install them:

```bash
fastmcp install claude-code server.py --with-requirements requirements.txt
```

**Editable packages**: For local packages under development, use `--with-editable` to install them in editable mode:

```bash
fastmcp install claude-code server.py --with-editable ./my-local-package
```

Alternatively, you can specify dependencies directly in your server code:

```python server.py
from fastmcp import FastMCP

mcp = FastMCP(
    name="Dice Roller",
    dependencies=["pandas", "requests"]
)
```

#### Python Version and Project Configuration

Control the Python environment for your server with these options:

**Python version**: Use `--python` to specify which Python version your server requires. This ensures compatibility when your server needs specific Python features:

```bash
fastmcp install claude-code server.py --python 3.11
```

**Project directory**: Use `--project` to run your server within a specific project context. This tells `uv` to use the project's configuration files and virtual environment:

```bash
fastmcp install claude-code server.py --project /path/to/my-project
```

#### Environment Variables

If your server needs environment variables (like API keys), you must include them:

```bash
fastmcp install claude-code server.py --server-name "Weather Server" \
  --env API_KEY=your-api-key \
  --env DEBUG=true
```

Or load them from a `.env` file:

```bash
fastmcp install claude-code server.py --server-name "Weather Server" --env-file .env
```

<Warning>
  **Claude Code must be installed**. The integration looks for the Claude Code CLI at the default installation location (`~/.claude/local/claude`) and uses the `claude mcp add` command to register servers.
</Warning>

### Manual Configuration

For more control over the configuration, you can manually use Claude Code's built-in MCP management commands. This gives you direct control over how your server is launched:

```bash
# Add a server with custom configuration
claude mcp add dice-roller -- uv run --with fastmcp fastmcp run server.py

# Add with environment variables
claude mcp add weather-server -e API_KEY=secret -e DEBUG=true -- uv run --with fastmcp fastmcp run server.py

# Add with specific scope (local, user, or project)
claude mcp add my-server --scope user -- uv run --with fastmcp fastmcp run server.py
```

You can also manually specify Python versions and project directories in your Claude Code commands:

```bash
# With specific Python version
claude mcp add ml-server -- uv run --python 3.11 --with fastmcp fastmcp run server.py

# Within a project directory
claude mcp add project-server -- uv run --project /path/to/project --with fastmcp fastmcp run server.py
```

## Using the Server

Once your server is installed, you can start using your FastMCP server with Claude Code.

Try asking Claude something like:

> "Roll some dice for me"

Claude will automatically detect your `roll_dice` tool and use it to fulfill your request, returning something like:

> I'll roll some dice for you! Here are your results: \[4, 2, 6]
>
> You rolled three dice and got a 4, a 2, and a 6!

Claude Code can now access all the tools, resources, and prompts you've defined in your FastMCP server.

If your server provides resources, you can reference them with `@` mentions using the format `@server:protocol://resource/path`. If your server provides prompts, you can use them as slash commands with `/mcp__servername__promptname`.


# Claude Desktop 🤝 FastMCP
Source: https://gofastmcp.com/integrations/claude-desktop

Call FastMCP servers from Claude Desktop

export const LocalFocusTip = () => {
  return <Tip>
            <strong>This integration focuses on running local FastMCP server files with STDIO transport.</strong> For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and <code>uv</code> commands.
        </Tip>;
};

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<LocalFocusTip />

Claude Desktop supports MCP servers through local STDIO connections and remote servers (beta), allowing you to extend Claude's capabilities with custom tools, resources, and prompts from your FastMCP servers.

<Note>
  Remote MCP server support is currently in beta and available for users on Claude Pro, Max, Team, and Enterprise plans (as of June 2025). Most users will still need to use local STDIO connections.
</Note>

<Note>
  This guide focuses specifically on using FastMCP servers with Claude Desktop. For general Claude Desktop MCP setup and official examples, see the [official Claude Desktop quickstart guide](https://modelcontextprotocol.io/quickstart/user).
</Note>

## Requirements

Claude Desktop traditionally requires MCP servers to run locally using STDIO transport, where your server communicates with Claude through standard input/output rather than HTTP. However, users on certain plans now have access to remote server support as well.

<Tip>
  If you don't have access to remote server support or need to connect to remote servers, you can create a **proxy server** that runs locally via STDIO and forwards requests to remote HTTP servers. See the [Proxy Servers](#proxy-servers) section below.
</Tip>

## Create a Server

The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run()
```

## Install the Server

### FastMCP CLI

<VersionBadge version="2.10.3" />

The easiest way to install a FastMCP server in Claude Desktop is using the `fastmcp install claude-desktop` command. This automatically handles the configuration and dependency management.

<Tip>
  Prior to version 2.10.3, Claude Desktop could be managed by running `fastmcp install <path>` without specifying the client.
</Tip>

```bash
fastmcp install claude-desktop server.py
```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:

```bash
# These are equivalent if your server object is named 'mcp'
fastmcp install claude-desktop server.py
fastmcp install claude-desktop server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install claude-desktop server.py:my_custom_server
```

After installation, restart Claude Desktop completely. You should see a hammer icon (🔨) in the bottom left of the input box, indicating that MCP tools are available.

#### Dependencies

FastMCP provides several ways to manage your server's dependencies when installing in Claude Desktop:

**Individual packages**: Use the `--with` flag to specify packages your server needs. You can use this flag multiple times:

```bash
fastmcp install claude-desktop server.py --with pandas --with requests
```

**Requirements file**: If you have a `requirements.txt` file listing all your dependencies, use `--with-requirements` to install them all at once:

```bash
fastmcp install claude-desktop server.py --with-requirements requirements.txt
```

**Editable packages**: For local packages in development, use `--with-editable` to install them in editable mode:

```bash
fastmcp install claude-desktop server.py --with-editable ./my-local-package
```

Alternatively, you can specify dependencies directly in your server code:

```python server.py
from fastmcp import FastMCP

mcp = FastMCP(
    name="Dice Roller",
    dependencies=["pandas", "requests"]
)
```

#### Python Version and Project Directory

FastMCP allows you to control the Python environment for your server:

**Python version**: Use `--python` to specify which Python version your server should run with. This is particularly useful when your server requires a specific Python version:

```bash
fastmcp install claude-desktop server.py --python 3.11
```

**Project directory**: Use `--project` to run your server within a specific project directory. This ensures that `uv` will discover all `pyproject.toml`, `uv.toml`, and `.python-version` files from that project:

```bash
fastmcp install claude-desktop server.py --project /path/to/my-project
```

When you specify a project directory, all relative paths in your server will be resolved from that directory, and the project's virtual environment will be used.

#### Environment Variables

<Warning>
  Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
</Warning>

If your server needs environment variables (like API keys), you must include them:

```bash
fastmcp install claude-desktop server.py --server-name "Weather Server" \
  --env API_KEY=your-api-key \
  --env DEBUG=true
```

Or load them from a `.env` file:

```bash
fastmcp install claude-desktop server.py --server-name "Weather Server" --env-file .env
```

<Warning>
  * **`uv` must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
  * **On macOS, it is recommended to install `uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.
</Warning>

### Manual Configuration

For more control over the configuration, you can manually edit Claude Desktop's configuration file. You can open the configuration file from Claude's developer settings, or find it in the following locations:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

The configuration file is a JSON object with a `mcpServers` key, which contains the configuration for each MCP server.

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "python",
      "args": ["path/to/your/server.py"]
    }
  }
}
```

After updating the configuration file, restart Claude Desktop completely. Look for the hammer icon (🔨) to confirm your server is loaded.

#### Dependencies

If your server has dependencies, you can use `uv` or another package manager to set up the environment.

When manually configuring dependencies, the recommended approach is to use `uv` with FastMCP. The configuration uses `uv run` to create an isolated environment with your specified packages:

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--with", "fastmcp",
        "--with", "pandas",
        "--with", "requests", 
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}
```

You can also manually specify Python versions and project directories in your configuration. Add `--python` to use a specific Python version, or `--project` to run within a project directory:

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--python", "3.11",
        "--project", "/path/to/project",
        "--with", "fastmcp",
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}
```

The order of arguments matters: Python version and project settings come before package specifications, which come before the actual command to run.

<Warning>
  * **`uv` must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
  * **On macOS, it is recommended to install `uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.
</Warning>

#### Environment Variables

You can also specify environment variables in the configuration:

```json
{
  "mcpServers": {
    "weather-server": {
      "command": "python",
      "args": ["path/to/weather_server.py"],
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}
```

<Warning>
  Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
</Warning>

## Remote Servers

Users on Claude Pro, Max, Team, and Enterprise plans have first-class remote server support via integrations. For other users, or as an alternative approach, FastMCP can create a proxy server that forwards requests to a remote HTTP server. You can install the proxy server in Claude Desktop.

Create a proxy server that connects to a remote HTTP server:

```python proxy_server.py
from fastmcp import FastMCP

# Create a proxy to a remote server
proxy = FastMCP.as_proxy(
    "https://example.com/mcp/sse", 
    name="Remote Server Proxy"
)

if __name__ == "__main__":
    proxy.run()  # Runs via STDIO for Claude Desktop
```

### Authentication

For authenticated remote servers, create an authenticated client following the guidance in the [client auth documentation](/clients/auth/bearer) and pass it to the proxy:

```python auth_proxy_server.py {7}
from fastmcp import FastMCP, Client
from fastmcp.client.auth import BearerAuth

# Create authenticated client
client = Client(
    "https://api.example.com/mcp/sse",
    auth=BearerAuth(token="your-access-token")
)

# Create proxy using the authenticated client
proxy = FastMCP.as_proxy(client, name="Authenticated Proxy")

if __name__ == "__main__":
    proxy.run()
```


# Cursor 🤝 FastMCP
Source: https://gofastmcp.com/integrations/cursor

Install and use FastMCP servers in Cursor

export const LocalFocusTip = () => {
  return <Tip>
            <strong>This integration focuses on running local FastMCP server files with STDIO transport.</strong> For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and <code>uv</code> commands.
        </Tip>;
};

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<LocalFocusTip />

Cursor supports MCP servers through multiple transport methods including STDIO, SSE, and Streamable HTTP, allowing you to extend Cursor's AI assistant with custom tools, resources, and prompts from your FastMCP servers.

## Requirements

This integration uses STDIO transport to run your FastMCP server locally. For remote deployments, you can run your FastMCP server with HTTP or SSE transport and configure it directly in Cursor's settings.

## Create a Server

The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run()
```

## Install the Server

### FastMCP CLI

<VersionBadge version="2.10.3" />

The easiest way to install a FastMCP server in Cursor is using the `fastmcp install cursor` command. This automatically handles the configuration, dependency management, and opens Cursor with a deeplink to install the server.

```bash
fastmcp install cursor server.py
```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:

```bash
# These are equivalent if your server object is named 'mcp'
fastmcp install cursor server.py
fastmcp install cursor server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install cursor server.py:my_custom_server
```

After running the command, Cursor will open automatically and prompt you to install the server. The command will be `uv`, which is expected as this is a Python STDIO server. Click "Install" to confirm:

![Cursor install prompt](https://mintlify.s3.us-west-1.amazonaws.com/fastmcp/integrations/cursor-install-mcp.png)

#### Dependencies

FastMCP offers multiple ways to manage dependencies for your Cursor servers:

**Individual packages**: Use the `--with` flag to specify packages your server needs. You can use this flag multiple times:

```bash
fastmcp install cursor server.py --with pandas --with requests
```

**Requirements file**: For projects with a `requirements.txt` file, use `--with-requirements` to install all dependencies at once:

```bash
fastmcp install cursor server.py --with-requirements requirements.txt
```

**Editable packages**: When developing local packages, use `--with-editable` to install them in editable mode:

```bash
fastmcp install cursor server.py --with-editable ./my-local-package
```

Alternatively, you can specify dependencies directly in your server code:

```python server.py
from fastmcp import FastMCP

mcp = FastMCP(
    name="Dice Roller",
    dependencies=["pandas", "requests"]
)
```

#### Python Version and Project Configuration

Control your server's Python environment with these options:

**Python version**: Use `--python` to specify which Python version your server should use. This is essential when your server requires specific Python features:

```bash
fastmcp install cursor server.py --python 3.11
```

**Project directory**: Use `--project` to run your server within a specific project context. This ensures `uv` discovers all project configuration files and uses the correct virtual environment:

```bash
fastmcp install cursor server.py --project /path/to/my-project
```

#### Environment Variables

<Warning>
  Cursor runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
</Warning>

If your server needs environment variables (like API keys), you must include them:

```bash
fastmcp install cursor server.py --server-name "Weather Server" \
  --env API_KEY=your-api-key \
  --env DEBUG=true
```

Or load them from a `.env` file:

```bash
fastmcp install cursor server.py --server-name "Weather Server" --env-file .env
```

<Warning>
  **`uv` must be installed and available in your system PATH**. Cursor runs in its own isolated environment and needs `uv` to manage dependencies.
</Warning>

### Generate MCP JSON

<Note>
  **Use the first-class integration above for the best experience.** The MCP JSON generation is useful for advanced use cases, manual configuration, or integration with other tools.
</Note>

You can generate MCP JSON configuration for manual use:

```bash
# Generate configuration and output to stdout
fastmcp install mcp-json server.py --server-name "Dice Roller" --with pandas

# Copy configuration to clipboard for easy pasting
fastmcp install mcp-json server.py --server-name "Dice Roller" --copy
```

This generates the standard `mcpServers` configuration format that can be used with any MCP-compatible client.

### Manual Configuration

For more control over the configuration, you can manually edit Cursor's configuration file. The configuration file is located at:

* **All platforms**: `~/.cursor/mcp.json`

The configuration file is a JSON object with a `mcpServers` key, which contains the configuration for each MCP server.

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "python",
      "args": ["path/to/your/server.py"]
    }
  }
}
```

After updating the configuration file, your server should be available in Cursor.

#### Dependencies

If your server has dependencies, you can use `uv` or another package manager to set up the environment.

When manually configuring dependencies, the recommended approach is to use `uv` with FastMCP. The configuration should use `uv run` to create an isolated environment with your specified packages:

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--with", "fastmcp",
        "--with", "pandas",
        "--with", "requests", 
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}
```

You can also manually specify Python versions and project directories in your configuration:

```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--python", "3.11",
        "--project", "/path/to/project",
        "--with", "fastmcp",
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}
```

Note that the order of arguments is important: Python version and project settings should come before package specifications.

<Warning>
  **`uv` must be installed and available in your system PATH**. Cursor runs in its own isolated environment and needs `uv` to manage dependencies.
</Warning>

#### Environment Variables

You can also specify environment variables in the configuration:

```json
{
  "mcpServers": {
    "weather-server": {
      "command": "python",
      "args": ["path/to/weather_server.py"],
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}
```

<Warning>
  Cursor runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
</Warning>

## Using the Server

Once your server is installed, you can start using your FastMCP server with Cursor's AI assistant.

Try asking Cursor something like:

> "Roll some dice for me"

Cursor will automatically detect your `roll_dice` tool and use it to fulfill your request, returning something like:

> 🎲 Here are your dice rolls: 4, 6, 4
>
> You rolled 3 dice with a total of 14! The 6 was a nice high roll there!

The AI assistant can now access all the tools, resources, and prompts you've defined in your FastMCP server.


# Eunomia Authorization 🤝 FastMCP
Source: https://gofastmcp.com/integrations/eunomia-authorization

Add policy-based authorization to your FastMCP servers

Add **policy-based authorization** to your FastMCP servers with one-line code addition with the **[Eunomia][eunomia-github] authorization middleware**.

Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic JSON-based policies and obtain a comprehensive audit log of all access attempts and violations.

## How it Works

Exploiting FastMCP's [Middleware][fastmcp-middleare], the Eunomia middleware intercepts all MCP requests to your server and, then, automatically maps MCP methods to authorization checks.

### Listing Operations

The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.

```mermaid
sequenceDiagram
    participant MCPClient as MCP Client
    participant EunomiaMiddleware as Eunomia Middleware
    participant MCPServer as FastMCP Server
    participant EunomiaServer as Eunomia Server

    MCPClient->>EunomiaMiddleware: MCP Listing Request (e.g., tools/list)
    EunomiaMiddleware->>MCPServer: MCP Listing Request
    MCPServer-->>EunomiaMiddleware: MCP Listing Response
    EunomiaMiddleware->>EunomiaServer: Authorization Checks
    EunomiaServer->>EunomiaMiddleware: Authorization Decisions
    EunomiaMiddleware-->>MCPClient: Filtered MCP Listing Response
```

### Execution Operations

The middleware behaves as a firewall for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.

```mermaid
sequenceDiagram
    participant MCPClient as MCP Client
    participant EunomiaMiddleware as Eunomia Middleware
    participant MCPServer as FastMCP Server
    participant EunomiaServer as Eunomia Server

    MCPClient->>EunomiaMiddleware: MCP Execution Request (e.g., tools/call)
    EunomiaMiddleware->>EunomiaServer: Authorization Check
    EunomiaServer->>EunomiaMiddleware: Authorization Decision
    EunomiaMiddleware-->>MCPClient: MCP Unauthorized Error (if denied)
    EunomiaMiddleware->>MCPServer: MCP Execution Request (if allowed)
    MCPServer-->>EunomiaMiddleware: MCP Execution Response (if allowed)
    EunomiaMiddleware-->>MCPClient: MCP Execution Response (if allowed)
```

## Add Authorization to Your Server

<Note>
  Eunomia is an AI-specific standalone authorization server that handles policy decisions. You must have an Eunomia server running alongside your FastMCP server for the middleware to function.

  Run it in the background with Docker:

  ```bash
  docker run -d -p 8000:8000 ttommitt/eunomia-server:latest
  ```
</Note>

### Create a Server with Authorization

First, install the `eunomia-mcp` package:

```bash
pip install eunomia-mcp
```

Then create a FastMCP server and add the Eunomia middleware in one line:

```python server.py
from fastmcp import FastMCP
from eunomia_mcp import EunomiaMcpMiddleware

mcp = FastMCP("Secure FastMCP Server 🔒")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

middleware = EunomiaMcpMiddleware()
app = mcp.add_middleware(middleware)

if __name__ == "__main__":
    mcp.run()
```

### Configure Access Policies

Use the `eunomia-mcp` CLI in your terminal to manage your authorization policies:

```bash
# Create a default policy configuration file
eunomia-mcp init
```

This creates a policy file you can customize to control access to your MCP tools and resources.

```bash
# Once ready, validate your policy
eunomia-mcp validate mcp_policies.json

# And push it to the Eunomia server
eunomia-mcp push mcp_policies.json
```

### Run the Server

Start your FastMCP server normally:

```bash
python server.py
```

The middleware will now intercept all MCP requests and check them against your policies. Requests include agent identification through headers like `X-Agent-ID`, `X-User-ID`, `User-Agent`, or `Authorization` and an automatic mapping of MCP methods to authorization resources and actions.

<Tip>
  For detailed policy configuration, custom authentication, and advanced
  deployment patterns, visit the [Eunomia MCP Middleware
  repository][eunomia-mcp-github].
</Tip>

[eunomia-github]: https://github.com/whataboutyou-ai/eunomia

[eunomia-mcp-github]: https://github.com/whataboutyou-ai/eunomia/tree/main/pkgs/extensions/mcp

[fastmcp-middleare]: /servers/middleware


# FastAPI 🤝 FastMCP
Source: https://gofastmcp.com/integrations/fastapi

Integrate FastMCP with FastAPI applications

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<Tip>
  **New in 2.11**: FastMCP is introducing a next-generation OpenAPI parser. The new parser has greatly improved performance and compatibility, and is also easier to maintain. To enable it, set the environment variable `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`.

  The new parser is largely API-compatible with the existing implementation and will become the default in a future version. We encourage all users to test it and report any issues before it becomes the default.
</Tip>

FastMCP provides two powerful ways to integrate with FastAPI applications:

1. **[Generate an MCP server FROM your FastAPI app](#generating-an-mcp-server)** - Convert existing API endpoints into MCP tools
2. **[Mount an MCP server INTO your FastAPI app](#mounting-an-mcp-server)** - Add MCP functionality to your web application

<Tip>
  Generating MCP servers from OpenAPI is a great way to get started with FastMCP, but in practice LLMs achieve **significantly better performance** with well-designed and curated MCP servers than with auto-converted OpenAPI servers. This is especially true for complex APIs with many endpoints and parameters.

  We recommend using the FastAPI integration for bootstrapping and prototyping, not for mirroring your API to LLM clients. See the post [Stop Converting Your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp) for more details.
</Tip>

<Note>
  FastMCP does *not* include FastAPI as a dependency; you must install it separately to use this integration.
</Note>

## Example FastAPI Application

Throughout this guide, we'll use this e-commerce API as our example (click the `Copy` button to copy it for use with other code blocks):

```python [expandable]
# Copy this FastAPI server into other code blocks in this guide

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Models
class Product(BaseModel):
    name: str
    price: float
    category: str
    description: str | None = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    description: str | None = None

# Create FastAPI app
app = FastAPI(title="E-commerce API", version="1.0.0")

# In-memory database
products_db = {
    1: ProductResponse(
        id=1, name="Laptop", price=999.99, category="Electronics"
    ),
    2: ProductResponse(
        id=2, name="Mouse", price=29.99, category="Electronics"
    ),
    3: ProductResponse(
        id=3, name="Desk Chair", price=299.99, category="Furniture"
    ),
}
next_id = 4

@app.get("/products", response_model=list[ProductResponse])
def list_products(
    category: str | None = None,
    max_price: float | None = None,
) -> list[ProductResponse]:
    """List all products with optional filtering."""
    products = list(products_db.values())
    if category:
        products = [p for p in products if p.category == category]
    if max_price:
        products = [p for p in products if p.price <= max_price]
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    """Get a specific product by ID."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.post("/products", response_model=ProductResponse)
def create_product(product: Product):
    """Create a new product."""
    global next_id
    product_response = ProductResponse(id=next_id, **product.model_dump())
    products_db[next_id] = product_response
    next_id += 1
    return product_response

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: Product):
    """Update an existing product."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[product_id] = ProductResponse(
        id=product_id,
        **product.model_dump(),
    )
    return products_db[product_id]

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete a product."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[product_id]
    return {"message": "Product deleted"}
```

<Tip>
  All subsequent code examples in this guide assume you have the above FastAPI application code already defined. Each example builds upon this base application, `app`.
</Tip>

## Generating an MCP Server

<VersionBadge version="2.0.0" />

One of the most common ways to bootstrap an MCP server is to generate it from an existing FastAPI application. FastMCP will expose your FastAPI endpoints as MCP components (tools, by default) in order to expose your API to LLM clients.

### Basic Conversion

Convert the FastAPI app to an MCP server with a single line:

```python {5}
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP

# Convert to MCP server
mcp = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run()
```

### Adding Components

Your converted MCP server is a full FastMCP instance, meaning you can add new tools, resources, and other components to it just like you would with any other FastMCP instance.

```python {8-11}
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP

# Convert to MCP server
mcp = FastMCP.from_fastapi(app=app)

# Add a new tool
@mcp.tool
def get_product(product_id: int) -> ProductResponse:
    """Get a product by ID."""
    return products_db[product_id]

# Run the MCP server
if __name__ == "__main__":
    mcp.run()
```

### Interacting with the MCP Server

Once you've converted your FastAPI app to an MCP server, you can interact with it using the FastMCP client to test functionality before deploying it to an LLM-based application.

```python {3, }
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP
from fastmcp.client import Client
import asyncio

# Convert to MCP server
mcp = FastMCP.from_fastapi(app=app)

async def demo():
    async with Client(mcp) as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[t.name for t in tools]}")
        
        # Create a product
        result = await client.call_tool(
            "create_product_products_post",
            {
                "name": "Wireless Keyboard",
                "price": 79.99,
                "category": "Electronics",
                "description": "Bluetooth mechanical keyboard"
            }
        )
        print(f"Created product: {result.data}")
        
        # List electronics under $100
        result = await client.call_tool(
            "list_products_products_get",
            {"category": "Electronics", "max_price": 100}
        )
        print(f"Affordable electronics: {result.data}")

if __name__ == "__main__":
    asyncio.run(demo())
```

### Custom Route Mapping

Because FastMCP's FastAPI integration is based on its [OpenAPI integration](/integrations/openapi), you can customize how endpoints are converted to MCP components in exactly the same way. For example, here we use a `RouteMap` to map all GET requests to MCP resources, and all POST/PUT/DELETE requests to MCP tools:

```python
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

# If using experimental parser, import from experimental module:
# from fastmcp.experimental.server.openapi import RouteMap, MCPType

# Custom mapping rules
mcp = FastMCP.from_fastapi(
    app=app,
    route_maps=[
        # GET with path params → ResourceTemplates
        RouteMap(
            methods=["GET"], 
            pattern=r".*\{.*\}.*", 
            mcp_type=MCPType.RESOURCE_TEMPLATE
        ),
        # Other GETs → Resources
        RouteMap(
            methods=["GET"], 
            pattern=r".*", 
            mcp_type=MCPType.RESOURCE
        ),
        # POST/PUT/DELETE → Tools (default)
    ],
)

# Now:
# - GET /products → Resource
# - GET /products/{id} → ResourceTemplate
# - POST/PUT/DELETE → Tools
```

<Tip>
  To learn more about customizing the conversion process, see the [OpenAPI Integration guide](/integrations/openapi).
</Tip>

### Authentication and Headers

You can configure headers and other client options via the `httpx_client_kwargs` parameter. For example, to add authentication to your FastAPI app, you can pass a `headers` dictionary to the `httpx_client_kwargs` parameter:

```python {27-31}
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP

# Add authentication to your FastAPI app
from fastapi import Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return credentials.credentials

# Add a protected endpoint
@app.get("/admin/stats", dependencies=[Depends(verify_token)])
def get_admin_stats():
    return {
        "total_products": len(products_db),
        "categories": list(set(p.category for p in products_db.values()))
    }

# Create MCP server with authentication headers
mcp = FastMCP.from_fastapi(
    app=app,
    httpx_client_kwargs={
        "headers": {
            "Authorization": "Bearer secret-token",
        }
    }
)
```

## Mounting an MCP Server

<VersionBadge version="2.3.1" />

In addition to generating servers, FastMCP can facilitate adding MCP servers to your existing FastAPI application. You can do this by mounting the MCP ASGI application.

### Basic Mounting

To mount an MCP server, you can use the `http_app` method on your FastMCP instance. This will return an ASGI application that can be mounted to your FastAPI application.

```python {23-30}
from fastmcp import FastMCP
from fastapi import FastAPI

# Create MCP server
mcp = FastMCP("Analytics Tools")

@mcp.tool
def analyze_pricing(category: str) -> dict:
    """Analyze pricing for a category."""
    products = [p for p in products_db.values() if p.category == category]
    if not products:
        return {"error": f"No products in {category}"}
    
    prices = [p.price for p in products]
    return {
        "category": category,
        "avg_price": round(sum(prices) / len(prices), 2),
        "min": min(prices),
        "max": max(prices),
    }

# Create ASGI app from MCP server
mcp_app = mcp.http_app(path='/mcp')

# Key: Pass lifespan to FastAPI
app = FastAPI(title="E-commerce API", lifespan=mcp_app.lifespan)

# Mount the MCP server
app.mount("/analytics", mcp_app)

# Now: API at /products/*, MCP at /analytics/mcp/
```

## Offering an LLM-Friendly API

A common pattern is to generate an MCP server from your FastAPI app and mount it back into the same application. This provides an LLM-optimized interface alongside your regular API:

```python
# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP
from fastapi import FastAPI

# 1. Generate MCP server from your API
mcp = FastMCP.from_fastapi(app=app, name="E-commerce MCP")

# 2. Create the MCP's ASGI app
mcp_app = mcp.http_app(path='/mcp')

# 3. Mount it back into your FastAPI app
app = FastAPI(title="E-commerce API", lifespan=mcp_app.lifespan)
app.mount("/llm", mcp_app)

# Now you have:
# - Regular API: http://localhost:8000/products
# - LLM-friendly MCP: http://localhost:8000/llm/mcp/
# Both served from the same FastAPI application!
```

This approach lets you maintain a single codebase while offering both traditional REST endpoints and MCP-compatible endpoints for LLM clients.

## Key Considerations

### Operation IDs

FastAPI operation IDs become MCP component names. Always specify meaningful operation IDs:

```python
# Good - explicit operation_id
@app.get("/users/{user_id}", operation_id="get_user_by_id")
def get_user(user_id: int):
    return {"id": user_id}

# Less ideal - auto-generated name
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

### Lifespan Management

When mounting MCP servers, always pass the lifespan context:

```python
# Correct - lifespan passed
mcp_app = mcp.http_app(path='/mcp')
app = FastAPI(lifespan=mcp_app.lifespan)
app.mount("/mcp", mcp_app)

# Incorrect - missing lifespan
app = FastAPI()
app.mount("/mcp", mcp.http_app())  # Session manager won't initialize
```

### Combining Lifespans

If your FastAPI app already has a lifespan (for database connections, startup tasks, etc.), you can't simply replace it with the MCP lifespan. Instead, you need to create a new lifespan function that manages both contexts. This ensures that both your app's initialization logic and the MCP server's session manager run properly:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastmcp import FastMCP

# Your existing lifespan
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    print("Starting up the app...")
    # Initialize database, cache, etc.
    yield
    # Shutdown
    print("Shutting down the app...")

# Create MCP server
mcp = FastMCP("Tools")
mcp_app = mcp.http_app(path='/mcp')

# Combine both lifespans
@asynccontextmanager
async def combined_lifespan(app: FastAPI):
    # Run both lifespans
    async with app_lifespan(app):
        async with mcp_app.lifespan(app):
            yield

# Use the combined lifespan
app = FastAPI(lifespan=combined_lifespan)
app.mount("/mcp", mcp_app)
```

This pattern ensures both your app's initialization logic and the MCP server's session manager are properly managed. The key is using nested `async with` statements - the inner context (MCP) will be initialized after the outer context (your app), and cleaned up before it. This maintains the correct initialization and cleanup order for all your resources.

### Performance Tips

1. **Use in-memory transport for testing** - Pass MCP servers directly to clients
2. **Design purpose-built MCP tools** - Better than auto-converting complex APIs
3. **Keep tool parameters simple** - LLMs perform better with focused interfaces

For more details on configuration options, see the [OpenAPI Integration guide](/integrations/openapi).


# Gemini SDK 🤝 FastMCP
Source: https://gofastmcp.com/integrations/gemini

Call FastMCP servers from the Google Gemini SDK

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

Google's Gemini API includes built-in support for MCP servers in their Python and JavaScript SDKs, allowing you to connect directly to MCP servers and use their tools seamlessly with Gemini models.

## Gemini Python SDK

Google's [Gemini Python SDK](https://ai.google.dev/gemini-api/docs) can use FastMCP clients directly.

<Note>
  Google's MCP integration is currently experimental and available in the Python and JavaScript SDKs. The API automatically calls MCP tools when needed and can connect to both local and remote MCP servers.
</Note>

<Tip>
  Currently, Gemini's MCP support only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to the AI. Other MCP features like resources and prompts are not currently supported.
</Tip>

### Create a Server

First, create a FastMCP server with the tools you want to expose. For this example, we'll create a server with a single tool that rolls dice.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run()
```

### Call the Server

To use the Gemini API with MCP, you'll need to install the Google Generative AI SDK:

```bash
pip install google-genai
```

You'll also need to authenticate with Google. You can do this by setting the `GEMINI_API_KEY` environment variable. Consult the Gemini SDK documentation for more information.

```bash
export GEMINI_API_KEY="your-api-key"
```

Gemini's SDK interacts directly with the MCP client session. To call the server, you'll need to instantiate a FastMCP client, enter its connection context, and pass the client session to the Gemini SDK.

```python {5, 9, 15}
from fastmcp import Client
from google import genai
import asyncio

mcp_client = Client("server.py")
gemini_client = genai.Client()

async def main():    
    async with mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents="Roll 3 dice!",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session],  # Pass the FastMCP client session
            ),
        )
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

If you run this code, you'll see output like:

```text
Okay, I rolled 3 dice and got a 5, 4, and 1.
```

### Remote & Authenticated Servers

In the above example, we connected to our local server using `stdio` transport. Because we're using a FastMCP client, you can also connect to any local or remote MCP server, using any [transport](/clients/transports) or [auth](/clients/auth) method supported by FastMCP, simply by changing the client configuration.

For example, to connect to a remote, authenticated server, you can use the following client:

```python
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

mcp_client = Client(
    "https://my-server.com/mcp/",
    auth=BearerAuth("<your-token>"),
)
```

The rest of the code remains the same.


# MCP JSON Configuration 🤝 FastMCP
Source: https://gofastmcp.com/integrations/mcp-json-configuration

Generate standard MCP configuration files for any compatible client

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.10.3" />

FastMCP can generate standard MCP JSON configuration files that work with any MCP-compatible client including Claude Desktop, VS Code, Cursor, and other applications that support the Model Context Protocol.

## MCP JSON Configuration Standard

The MCP JSON configuration format is an **emergent standard** that has developed across the MCP ecosystem. This format defines how MCP clients should configure and launch MCP servers, providing a consistent way to specify server commands, arguments, and environment variables.

### Configuration Structure

The standard uses a `mcpServers` object where each key represents a server name and the value contains the server's configuration:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "executable",
      "args": ["arg1", "arg2"],
      "env": {
        "VAR": "value"
      }
    }
  }
}
```

### Server Configuration Fields

#### `command` (required)

The executable command to run the MCP server. This should be an absolute path or a command available in the system PATH.

```json
{
  "command": "python"
}
```

#### `args` (optional)

An array of command-line arguments passed to the server executable. Arguments are passed in order.

```json
{
  "args": ["server.py", "--verbose", "--port", "8080"]
}
```

#### `env` (optional)

An object containing environment variables to set when launching the server. All values must be strings.

```json
{
  "env": {
    "API_KEY": "secret-key",
    "DEBUG": "true",
    "PORT": "8080"
  }
}
```

### Client Adoption

This format is widely adopted across the MCP ecosystem:

* **Claude Desktop**: Uses `~/.claude/claude_desktop_config.json`
* **Cursor**: Uses `~/.cursor/mcp.json`
* **VS Code**: Uses workspace `.vscode/mcp.json`
* **Other clients**: Many MCP-compatible applications follow this standard

## Overview

<Note>
  **For the best experience, use FastMCP's first-class integrations:** [`fastmcp install claude-code`](/integrations/claude-code), [`fastmcp install claude-desktop`](/integrations/claude-desktop), or [`fastmcp install cursor`](/integrations/cursor). Use MCP JSON generation for advanced use cases and unsupported clients.
</Note>

The `fastmcp install mcp-json` command generates configuration in the standard `mcpServers` format used across the MCP ecosystem. This is useful when:

* **Working with unsupported clients** - Any MCP client not directly integrated with FastMCP
* **CI/CD environments** - Automated configuration generation for deployments
* **Configuration sharing** - Easy distribution of server setups to team members
* **Custom tooling** - Integration with your own MCP management tools
* **Manual setup** - When you prefer to manually configure your MCP client

## Basic Usage

Generate configuration and output to stdout (useful for piping):

```bash
fastmcp install mcp-json server.py
```

This outputs the server configuration JSON with the server name as the root key:

```json
{
  "My Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp", 
      "fastmcp",
      "run",
      "/absolute/path/to/server.py"
    ]
  }
}
```

To use this in a client configuration file, add it to the `mcpServers` object in your client's configuration:

```json
{
  "mcpServers": {
    "My Server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp", 
        "fastmcp",
        "run",
        "/absolute/path/to/server.py"
      ]
    }
  }
}
```

<Note>
  When using `--python`, `--project`, or `--with-requirements`, the generated configuration will include these options in the `uv run` command, ensuring your server runs with the correct Python version and dependencies.
</Note>

<Note>
  Different MCP clients may have specific configuration requirements or formatting needs. Always consult your client's documentation to ensure proper integration.
</Note>

## Configuration Options

### Server Naming

```bash
# Use server's built-in name (from FastMCP constructor)
fastmcp install mcp-json server.py

# Override with custom name
fastmcp install mcp-json server.py --name "Custom Server Name"
```

### Dependencies

Add Python packages your server needs:

```bash
# Single package
fastmcp install mcp-json server.py --with pandas

# Multiple packages  
fastmcp install mcp-json server.py --with pandas --with requests --with httpx

# Editable local package
fastmcp install mcp-json server.py --with-editable ./my-package

# From requirements file
fastmcp install mcp-json server.py --with-requirements requirements.txt
```

You can also specify dependencies directly in your server code:

```python server.py
from fastmcp import FastMCP

mcp = FastMCP(
    name="Data Analysis Server",
    dependencies=["pandas", "matplotlib", "seaborn"]
)
```

### Environment Variables

```bash
# Individual environment variables
fastmcp install mcp-json server.py \
  --env API_KEY=your-secret-key \
  --env DEBUG=true

# Load from .env file
fastmcp install mcp-json server.py --env-file .env
```

### Python Version and Project Directory

Specify Python version or run within a specific project:

```bash
# Use specific Python version
fastmcp install mcp-json server.py --python 3.11

# Run within a project directory
fastmcp install mcp-json server.py --project /path/to/project
```

### Server Object Selection

Use the same `file.py:object` notation as other FastMCP commands:

```bash
# Auto-detects server object (looks for 'mcp', 'server', or 'app')
fastmcp install mcp-json server.py

# Explicit server object
fastmcp install mcp-json server.py:my_custom_server
```

## Clipboard Integration

Copy configuration directly to your clipboard for easy pasting:

```bash
fastmcp install mcp-json server.py --copy
```

<Note>
  The `--copy` flag requires the `pyperclip` Python package. If not installed, you'll see an error message with installation instructions.
</Note>

## Usage Examples

### Basic Server

```bash
fastmcp install mcp-json dice_server.py
```

Output:

```json
{
  "Dice Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp", 
      "run",
      "/home/user/dice_server.py"
    ]
  }
}
```

### Production Server with Dependencies

```bash
fastmcp install mcp-json api_server.py \
  --name "Production API Server" \
  --with requests \
  --with python-dotenv \
  --env API_BASE_URL=https://api.example.com \
  --env TIMEOUT=30
```

### Advanced Configuration

```bash
fastmcp install mcp-json ml_server.py \
  --name "ML Analysis Server" \
  --python 3.11 \
  --with-requirements requirements.txt \
  --project /home/user/ml-project \
  --env GPU_DEVICE=0
```

Output:

```json
{
  "Production API Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "--with",
      "python-dotenv", 
      "--with",
      "requests",
      "fastmcp",
      "run", 
      "/home/user/api_server.py"
    ],
    "env": {
      "API_BASE_URL": "https://api.example.com",
      "TIMEOUT": "30"
    }
  }
}
```

The advanced configuration example generates:

```json
{
  "ML Analysis Server": {
    "command": "uv",
    "args": [
      "run",
      "--python",
      "3.11",
      "--project",
      "/home/user/ml-project",
      "--with",
      "fastmcp",
      "--with-requirements",
      "requirements.txt",
      "fastmcp",
      "run",
      "/home/user/ml_server.py"
    ],
    "env": {
      "GPU_DEVICE": "0"
    }
  }
}
```

### Pipeline Usage

Save configuration to file:

```bash
fastmcp install mcp-json server.py > mcp-config.json
```

Use in shell scripts:

```bash
#!/bin/bash
CONFIG=$(fastmcp install mcp-json server.py --name "CI Server")
echo "$CONFIG" | jq '."CI Server".command'
# Output: "uv"
```

## Integration with MCP Clients

The generated configuration works with any MCP-compatible application:

### Claude Desktop

<Note>
  **Prefer [`fastmcp install claude-desktop`](/integrations/claude-desktop)** for automatic installation. Use MCP JSON for advanced configuration needs.
</Note>

Copy the `mcpServers` object into `~/.claude/claude_desktop_config.json`

### Cursor

<Note>
  **Prefer [`fastmcp install cursor`](/integrations/cursor)** for automatic installation. Use MCP JSON for advanced configuration needs.
</Note>

Add to `~/.cursor/mcp.json`

### VS Code

Add to your workspace's `.vscode/mcp.json` file

### Custom Applications

Use the JSON configuration with any application that supports the MCP protocol

## Configuration Format

The generated configuration outputs a server object with the server name as the root key:

```json
{
  "<server-name>": {
    "command": "<executable>",
    "args": ["<arg1>", "<arg2>", "..."],
    "env": {
      "<ENV_VAR>": "<value>"
    }
  }
}
```

To use this in an MCP client, add it to the client's `mcpServers` configuration object.

**Fields:**

* `command`: The executable to run (always `uv` for FastMCP servers)
* `args`: Command-line arguments including dependencies and server path
* `env`: Environment variables (only included if specified)

<Warning>
  **All file paths in the generated configuration are absolute paths**. This ensures the configuration works regardless of the working directory when the MCP client starts the server.
</Warning>

## Requirements

* **uv**: Must be installed and available in your system PATH
* **pyperclip** (optional): Required only for `--copy` functionality

Install uv if not already available:

```bash
# macOS
brew install uv

# Linux/Windows  
curl -LsSf https://astral.sh/uv/install.sh | sh
```


# OpenAI API 🤝 FastMCP
Source: https://gofastmcp.com/integrations/openai

Call FastMCP servers from the OpenAI API

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

## Responses API

OpenAI's [Responses API](https://platform.openai.com/docs/api-reference/responses) supports [MCP servers](https://platform.openai.com/docs/guides/tools-remote-mcp) as remote tool sources, allowing you to extend AI capabilities with custom functions.

<Note>
  The Responses API is a distinct API from OpenAI's Completions API or Assistants API. At this time, only the Responses API supports MCP.
</Note>

<Tip>
  Currently, the Responses API only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to the AI agent. Other MCP features like resources and prompts are not currently supported.
</Tip>

### Create a Server

First, create a FastMCP server with the tools you want to expose. For this example, we'll create a server with a single tool that rolls dice.

```python server.py
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
```

### Deploy the Server

Your server must be deployed to a public URL in order for OpenAI to access it.

For development, you can use tools like `ngrok` to temporarily expose a locally-running server to the internet. We'll do that for this example (you may need to install `ngrok` and create a free account), but you can use any other method to deploy your server.

Assuming you saved the above code as `server.py`, you can run the following two commands in two separate terminals to deploy your server and expose it to the internet:

<CodeGroup>
  ```bash FastMCP server
  python server.py
  ```

  ```bash ngrok
  ngrok http 8000
  ```
</CodeGroup>

<Warning>
  This exposes your unauthenticated server to the internet. Only run this command in a safe environment if you understand the risks.
</Warning>

### Call the Server

To use the Responses API, you'll need to install the OpenAI Python SDK (not included with FastMCP):

```bash
pip install openai
```

You'll also need to authenticate with OpenAI. You can do this by setting the `OPENAI_API_KEY` environment variable. Consult the OpenAI SDK documentation for more information.

```bash
export OPENAI_API_KEY="your-api-key"
```

Here is an example of how to call your server from Python. Note that you'll need to replace `https://your-server-url.com` with the actual URL of your server. In addition, we use `/mcp/` as the endpoint because we deployed a streamable-HTTP server with the default path; you may need to use a different endpoint if you customized your server's deployment.

```python {4, 11-16}
from openai import OpenAI

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "dice_server",
            "server_url": f"{url}/mcp/",
            "require_approval": "never",
        },
    ],
    input="Roll a few dice!",
)

print(resp.output_text)
```

If you run this code, you'll see something like the following output:

```text
You rolled 3 dice and got the following results: 6, 4, and 2!
```

### Authentication

<VersionBadge version="2.6.0" />

The Responses API can include headers to authenticate the request, which means you don't have to worry about your server being publicly accessible.

#### Server Authentication

The simplest way to add authentication to the server is to use a bearer token scheme.

For this example, we'll quickly generate our own tokens with FastMCP's `RSAKeyPair` utility, but this may not be appropriate for production use. For more details, see the complete server-side [Bearer Auth](/servers/auth/bearer) documentation.

We'll start by creating an RSA key pair to sign and verify tokens.

```python
from fastmcp.server.auth.providers.bearer import RSAKeyPair

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")
```

<Warning>
  FastMCP's `RSAKeyPair` utility is for development and testing only.
</Warning>

Next, we'll create a `BearerAuthProvider` to authenticate the server.

```python
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)
```

Here is a complete example that you can copy/paste. For simplicity and the purposes of this example only, it will print the token to the console. **Do NOT do this in production!**

```python server.py [expandable]
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair
import random

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="dice-server")

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    audience="dice-server",
)

mcp = FastMCP(name="Dice Roller", auth=auth)

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    print(f"\n---\n\n🔑 Dice Roller access token:\n\n{access_token}\n\n---\n")
    mcp.run(transport="http", port=8000)
```

#### Client Authentication

If you try to call the authenticated server with the same OpenAI code we wrote earlier, you'll get an error like this:

```python
pythonAPIStatusError: Error code: 424 - {
    "error": {
        "message": "Error retrieving tool list from MCP server: 'dice_server'. Http status code: 401 (Unauthorized)",
        "type": "external_connector_error",
        "param": "tools",
        "code": "http_error"
    }
}
```

As expected, the server is rejecting the request because it's not authenticated.

To authenticate the client, you can pass the token in the `Authorization` header with the `Bearer` scheme:

```python {4, 7, 19-21} [expandable]
from openai import OpenAI

# Your server URL (replace with your actual URL)
url = 'https://your-server-url.com'

# Your access token (replace with your actual token)
access_token = 'your-access-token'

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "dice_server",
            "server_url": f"{url}/mcp/",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {access_token}"
            }
        },
    ],
    input="Roll a few dice!",
)

print(resp.output_text)
```

You should now see the dice roll results in the output.


# OpenAPI 🤝 FastMCP
Source: https://gofastmcp.com/integrations/openapi

Generate MCP servers from any OpenAPI specification

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.0.0" />

<Tip>
  **New in 2.11**: FastMCP is introducing a next-generation OpenAPI parser. The new parser has greatly improved performance and compatibility, and is also easier to maintain. To enable it, set the environment variable `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`.

  The new parser is largely API-compatible with the existing implementation and will become the default in a future version. We encourage all users to test it and report any issues before it becomes the default.
</Tip>

FastMCP can automatically generate an MCP server from any OpenAPI specification, allowing AI models to interact with existing APIs through the MCP protocol. Instead of manually creating tools and resources, you provide an OpenAPI spec and FastMCP intelligently converts API endpoints into the appropriate MCP components.

<Tip>
  Generating MCP servers from OpenAPI is a great way to get started with FastMCP, but in practice LLMs achieve **significantly better performance** with well-designed and curated MCP servers than with auto-converted OpenAPI servers. This is especially true for complex APIs with many endpoints and parameters.

  We recommend using the FastAPI integration for bootstrapping and prototyping, not for mirroring your API to LLM clients. See the post [Stop Converting Your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp) for more details.
</Tip>

## Create a Server

To convert an OpenAPI specification to an MCP server, use the `FastMCP.from_openapi()` class method:

```python server.py
import httpx
from fastmcp import FastMCP

# Create an HTTP client for your API
client = httpx.AsyncClient(base_url="https://api.example.com")

# Load your OpenAPI spec 
openapi_spec = httpx.get("https://api.example.com/openapi.json").json()

# Create the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="My API Server"
)

if __name__ == "__main__":
    mcp.run()
```

### Authentication

If your API requires authentication, configure it on the HTTP client:

```python
import httpx
from fastmcp import FastMCP

# Bearer token authentication
api_client = httpx.AsyncClient(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

# Create MCP server with authenticated client
mcp = FastMCP.from_openapi(
    openapi_spec=spec, 
    client=api_client,
    timeout=30.0  # 30 second timeout for all requests
)
```

## Route Mapping

By default, FastMCP converts **every endpoint** in your OpenAPI specification into an MCP **Tool**. This provides a simple, predictable starting point that ensures all your API's functionality is immediately available to the vast majority of LLM clients which only support MCP tools.

While this is a pragmatic default for maximum compatibility, you can easily customize this behavior. Internally, FastMCP uses an ordered list of `RouteMap` objects to determine how to map OpenAPI routes to various MCP component types.

Each `RouteMap` specifies a combination of methods, patterns, and tags, as well as a corresponding MCP component type. Each OpenAPI route is checked against each `RouteMap` in order, and the first one that matches every criteria is used to determine its converted MCP type. A special type, `EXCLUDE`, can be used to exclude routes from the MCP server entirely.

* **Methods**: HTTP methods to match (e.g. `["GET", "POST"]` or `"*"` for all)
* **Pattern**: Regex pattern to match the route path (e.g. `r"^/users/.*"` or `r".*"` for all)
* **Tags**: A set of OpenAPI tags that must all be present. An empty set (`{}`) means no tag filtering, so the route matches regardless of its tags.
* **MCP type**: What MCP component type to create (`TOOL`, `RESOURCE`, `RESOURCE_TEMPLATE`, or `EXCLUDE`)
* **MCP tags**: A set of custom tags to add to components created from matching routes

Here is FastMCP's default rule:

```python
from fastmcp.server.openapi import RouteMap, MCPType

DEFAULT_ROUTE_MAPPINGS = [
    # All routes become tools
    RouteMap(mcp_type=MCPType.TOOL),
]
```

<Tip>
  **Experimental Parser**: If you're using the new parser (enabled via `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`), import from the experimental module instead:

  ```python
  from fastmcp.experimental.server.openapi import RouteMap, MCPType
  ```

  The API is identical, but the implementation provides better performance and serverless compatibility.
</Tip>

### Custom Route Maps

When creating your FastMCP server, you can customize routing behavior by providing your own list of `RouteMap` objects. Your custom maps are processed before the default route maps, and routes will be assigned to the first matching custom map.

For example, prior to FastMCP 2.8.0, GET requests were automatically mapped to `Resource` and `ResourceTemplate` components based on whether they had path parameters. (This was changed solely for client compatibility reasons.) You can restore this behavior by providing custom route maps:

```python
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

# Restore pre-2.8.0 semantic mapping
semantic_maps = [
    # GET requests with path parameters become ResourceTemplates
    RouteMap(methods=["GET"], pattern=r".*\{.*\}.*", mcp_type=MCPType.RESOURCE_TEMPLATE),
    # All other GET requests become Resources
    RouteMap(methods=["GET"], pattern=r".*", mcp_type=MCPType.RESOURCE),
]

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_maps=semantic_maps,
)
```

With these maps, `GET` requests are handled semantically, and all other methods (`POST`, `PUT`, etc.) will fall through to the default rule and become `Tool`s.

Here is a more complete example that uses custom route maps to convert all `GET` endpoints under `/analytics/` to tools while excluding all admin endpoints and all routes tagged "internal". All other routes will be handled by the default rules:

```python
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_maps=[
        # Analytics `GET` endpoints are tools
        RouteMap(
            methods=["GET"], 
            pattern=r"^/analytics/.*", 
            mcp_type=MCPType.TOOL,
        ),

        # Exclude all admin endpoints
        RouteMap(
            pattern=r"^/admin/.*", 
            mcp_type=MCPType.EXCLUDE,
        ),

        # Exclude all routes tagged "internal"
        RouteMap(
            tags={"internal"},
            mcp_type=MCPType.EXCLUDE,
        ),
    ],
)
```

<Tip>
  The default route maps are always applied after your custom maps, so you do not have to create route maps for every possible route.
</Tip>

### Excluding Routes

To exclude routes from the MCP server, use a route map to assign them to `MCPType.EXCLUDE`.

You can use this to remove sensitive or internal routes by targeting them specifically:

```python
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_maps=[
        RouteMap(pattern=r"^/admin/.*", mcp_type=MCPType.EXCLUDE),
        RouteMap(tags={"internal"}, mcp_type=MCPType.EXCLUDE),
    ],
)
```

Or you can use a catch-all rule to exclude everything that your maps don't handle explicitly:

```python
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_maps=[
        # custom mapping logic goes here
        # ... your specific route maps ...
        # exclude all remaining routes
        RouteMap(mcp_type=MCPType.EXCLUDE),
    ],
)
```

<Tip>
  Using a catch-all exclusion rule will prevent the default route mappings from being applied, since it will match every remaining route. This is useful if you want to explicitly allow-list certain routes.
</Tip>

### Advanced Route Mapping

<VersionBadge version="2.5.0" />

For advanced use cases that require more complex logic, you can provide a `route_map_fn` callable. After the route map logic is applied, this function is called on each matched route and its assigned MCP component type. It can optionally return a different component type to override the mapped assignment. If it returns `None`, the assigned type is used.

In addition to more precise targeting of methods, patterns, and tags, this function can access any additional OpenAPI metadata about the route.

<Tip>
  The `route_map_fn` **is** called on routes that matched `MCPType.EXCLUDE` in your custom maps, giving you an opportunity to override the exclusion.
</Tip>

```python
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType, HTTPRoute

def custom_route_mapper(route: HTTPRoute, mcp_type: MCPType) -> MCPType | None:
    """Advanced route type mapping."""
    # Convert all admin routes to tools regardless of HTTP method
    if "/admin/" in route.path:
        return MCPType.TOOL

    elif "internal" in route.tags:
        return MCPType.EXCLUDE
    
    # Convert user detail routes to templates even if they're POST
    elif route.path.startswith("/users/") and route.method == "POST":
        return MCPType.RESOURCE_TEMPLATE
    
    # Use defaults for all other routes
    return None

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_map_fn=custom_route_mapper,
)
```

## Customization

### Component Names

<VersionBadge version="2.5.0" />

FastMCP automatically generates names for MCP components based on the OpenAPI specification. By default, it uses the `operationId` from your OpenAPI spec, up to the first double underscore (`__`).

All component names are automatically:

* **Slugified**: Spaces and special characters are converted to underscores or removed
* **Truncated**: Limited to 56 characters maximum to ensure compatibility
* **Unique**: If multiple components have the same name, a number is automatically appended to make them unique

For more control over component names, you can provide an `mcp_names` dictionary that maps `operationId` values to your desired names. The `operationId` must be exactly as it appears in the OpenAPI spec. The provided name will always be slugified and truncated.

```python
mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    mcp_names={
        "list_users__with_pagination": "user_list",
        "create_user__admin_required": "create_user", 
        "get_user_details__admin_required": "user_detail",
    }
)
```

Any `operationId` not found in `mcp_names` will use the default strategy (operationId up to the first `__`).

### Tags

<VersionBadge version="2.8.0" />

FastMCP provides several ways to add tags to your MCP components, allowing you to categorize and organize them for better discoverability and filtering. Tags are combined from multiple sources to create the final set of tags on each component.

#### RouteMap Tags

You can add custom tags to components created from specific routes using the `mcp_tags` parameter in `RouteMap`. These tags will be applied to all components created from routes that match that particular route map.

```python
from fastmcp.server.openapi import RouteMap, MCPType

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    route_maps=[
        # Add custom tags to all POST endpoints
        RouteMap(
            methods=["POST"],
            pattern=r".*",
            mcp_type=MCPType.TOOL,
            mcp_tags={"write-operation", "api-mutation"}
        ),
        
        # Add different tags to detail view endpoints
        RouteMap(
            methods=["GET"],
            pattern=r".*\{.*\}.*",
            mcp_type=MCPType.RESOURCE_TEMPLATE,
            mcp_tags={"detail-view", "parameterized"}
        ),
        
        # Add tags to list endpoints
        RouteMap(
            methods=["GET"],
            pattern=r".*",
            mcp_type=MCPType.RESOURCE,
            mcp_tags={"list-data", "collection"}
        ),
    ],
)
```

#### Global Tags

You can add tags to **all** components by providing a `tags` parameter when creating your MCP server. These global tags will be applied to every component created from your OpenAPI specification.

```python
mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    tags={"api-v2", "production", "external"}
)
```

### Advanced Customization

<VersionBadge version="2.5.0" />

By default, FastMCP creates MCP components using a variety of metadata from the OpenAPI spec, such as incorporating the OpenAPI description into the MCP component description.

At times you may want to modify those MCP components in a variety of ways, such as adding LLM-specific instructions or tags. For fine-grained customization, you can provide a `mcp_component_fn` when creating the MCP server. After each MCP component has been created, this function is called on it and has the opportunity to modify it in-place.

<Tip>
  Your `mcp_component_fn` is expected to modify the component in-place, not to return a new component. The result of the function is ignored.
</Tip>

```python
from fastmcp.server.openapi import (
    HTTPRoute, 
    OpenAPITool, 
    OpenAPIResource, 
    OpenAPIResourceTemplate,
)

# If using experimental parser, import from experimental module:
# from fastmcp.experimental.server.openapi import (
#     HTTPRoute,
#     OpenAPITool,
#     OpenAPIResource,
#     OpenAPIResourceTemplate,
# )

def customize_components(
    route: HTTPRoute, 
    component: OpenAPITool | OpenAPIResource | OpenAPIResourceTemplate,
) -> None:
    # Add custom tags to all components
    component.tags.add("openapi")
    
    # Customize based on component type
    if isinstance(component, OpenAPITool):
        component.description = f"🔧 {component.description} (via API)"
    
    if isinstance(component, OpenAPIResource):
        component.description = f"📊 {component.description}"
        component.tags.add("data")

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=client,
    mcp_component_fn=customize_components,
)
```

## Request Parameter Handling

FastMCP intelligently handles different types of parameters in OpenAPI requests:

### Query Parameters

By default, FastMCP only includes query parameters that have non-empty values. Parameters with `None` values or empty strings are automatically filtered out.

```python
# When calling this tool...
await client.call_tool("search_products", {
    "category": "electronics",  # ✅ Included
    "min_price": 100,           # ✅ Included  
    "max_price": None,          # ❌ Excluded
    "brand": "",                # ❌ Excluded
})

# The HTTP request will be: GET /products?category=electronics&min_price=100
```

### Path Parameters

Path parameters are typically required by REST APIs. FastMCP:

* Filters out `None` values
* Validates that all required path parameters are provided
* Raises clear errors for missing required parameters

```python
# ✅ This works
await client.call_tool("get_user", {"user_id": 123})

# ❌ This raises: "Missing required path parameters: {'user_id'}"
await client.call_tool("get_user", {"user_id": None})
```

### Array Parameters

FastMCP handles array parameters according to OpenAPI specifications:

* **Query arrays**: Serialized based on the `explode` parameter (default: `True`)
* **Path arrays**: Serialized as comma-separated values (OpenAPI 'simple' style)

```python
# Query array with explode=true (default)
# ?tags=red&tags=blue&tags=green

# Query array with explode=false  
# ?tags=red,blue,green

# Path array (always comma-separated)
# /items/red,blue,green
```

### Headers

Header parameters are automatically converted to strings and included in the HTTP request.


# Permit.io Authorization 🤝 FastMCP
Source: https://gofastmcp.com/integrations/permit

Add fine-grained authorization to your FastMCP servers with Permit.io

Add **policy-based authorization** to your FastMCP servers with one-line code addition with the **[Permit.io][permit-github] authorization middleware**.

Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic policies using Permit.io's powerful RBAC, ABAC, and REBAC capabilities, and obtain comprehensive audit logs of all access attempts and violations.

## How it Works

Leveraging FastMCP's [Middleware][fastmcp-middleware], the Permit.io middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks against your Permit.io policies; covering both server methods and tool execution.

### Policy Mapping

The middleware automatically maps MCP methods to Permit.io resources and actions:

* **MCP server methods** (e.g., `tools/list`, `resources/read`):
  * **Resource**: `{server_name}_{component}` (e.g., `myserver_tools`)
  * **Action**: The method verb (e.g., `list`, `read`)
* **Tool execution** (method `tools/call`):
  * **Resource**: `{server_name}` (e.g., `myserver`)
  * **Action**: The tool name (e.g., `greet`)

![Permit.io Policy Mapping Example](https://mintlify.s3.us-west-1.amazonaws.com/fastmcp/integrations/images/policy_mapping.png)

*Example: In Permit.io, the 'Admin' role is granted permissions on resources and actions as mapped by the middleware. For example, 'greet', 'greet-jwt', and 'login' are actions on the 'mcp\_server' resource, and 'list' is an action on the 'mcp\_server\_tools' resource.*

> **Note:**
> Don't forget to assign the relevant role (e.g., Admin, User) to the user authenticating to your MCP server (such as the user in the JWT) in the Permit.io Directory. Without the correct role assignment, users will not have access to the resources and actions you've configured in your policies.
>
> ![Permit.io Directory Role Assignment Example](https://mintlify.s3.us-west-1.amazonaws.com/fastmcp/integrations/images/role_assignement.png)
>
> *Example: In Permit.io Directory, both 'client' and 'admin' users are assigned the 'Admin' role, granting them the permissions defined in your policy mapping.*

For detailed policy mapping examples and configuration, see [Detailed Policy Mapping](https://github.com/permitio/permit-fastmcp/blob/main/docs/policy-mapping.md).

### Listing Operations

The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.

```mermaid
sequenceDiagram
    participant MCPClient as MCP Client
    participant PermitMiddleware as Permit.io Middleware
    participant MCPServer as FastMCP Server
    participant PermitPDP as Permit.io PDP

    MCPClient->>PermitMiddleware: MCP Listing Request (e.g., tools/list)
    PermitMiddleware->>MCPServer: MCP Listing Request
    MCPServer-->>PermitMiddleware: MCP Listing Response
    PermitMiddleware->>PermitPDP: Authorization Checks
    PermitPDP->>PermitMiddleware: Authorization Decisions
    PermitMiddleware-->>MCPClient: Filtered MCP Listing Response
```

### Execution Operations

The middleware behaves as an enforcement point for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.

```mermaid
sequenceDiagram
    participant MCPClient as MCP Client
    participant PermitMiddleware as Permit.io Middleware
    participant MCPServer as FastMCP Server
    participant PermitPDP as Permit.io PDP

    MCPClient->>PermitMiddleware: MCP Execution Request (e.g., tools/call)
    PermitMiddleware->>PermitPDP: Authorization Check
    PermitPDP->>PermitMiddleware: Authorization Decision
    PermitMiddleware-->>MCPClient: MCP Unauthorized Error (if denied)
    PermitMiddleware->>MCPServer: MCP Execution Request (if allowed)
    MCPServer-->>PermitMiddleware: MCP Execution Response (if allowed)
    PermitMiddleware-->>MCPClient: MCP Execution Response (if allowed)
```

## Add Authorization to Your Server

<Note>
  Permit.io is a cloud-native authorization service. You need a Permit.io account and a running Policy Decision Point (PDP) for the middleware to function. You can run the PDP locally with Docker or use Permit.io's cloud PDP.
</Note>

### Prerequisites

1. **Permit.io Account**: Sign up at [permit.io](https://permit.io)
2. **PDP Setup**: Run the Permit.io PDP locally or use the cloud PDP (RBAC only)
3. **API Key**: Get your Permit.io API key from the dashboard

### Run the Permit.io PDP

Run the PDP locally with Docker:

```bash
docker run -p 7766:7766 permitio/pdp:latest
```

Or use the cloud PDP URL: `https://cloudpdp.api.permit.io`

### Create a Server with Authorization

First, install the `permit-fastmcp` package:

```bash
# Using UV (recommended)
uv add permit-fastmcp

# Using pip
pip install permit-fastmcp
```

Then create a FastMCP server and add the Permit.io middleware:

```python server.py
from fastmcp import FastMCP
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware

mcp = FastMCP("Secure FastMCP Server 🔒")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add Permit.io authorization middleware
mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))

if __name__ == "__main__":
    mcp.run(transport="http")
```

### Configure Access Policies

Create your authorization policies in the Permit.io dashboard:

1. **Create Resources**: Define resources like `mcp_server` and `mcp_server_tools`
2. **Define Actions**: Add actions like `greet`, `add`, `list`, `read`
3. **Create Roles**: Define roles like `Admin`, `User`, `Guest`
4. **Assign Permissions**: Grant roles access to specific resources and actions
5. **Assign Users**: Assign roles to users in the Permit.io Directory

For step-by-step setup instructions and troubleshooting, see [Getting Started & FAQ](https://github.com/permitio/permit-fastmcp/blob/main/docs/getting-started.md).

#### Example Policy Configuration

Policies are defined in the Permit.io dashboard, but you can also use the [Permit.io Terraform provider](https://github.com/permitio/terraform-provider-permitio) to define policies in code.

```terraform
# Resources
resource "permitio_resource" "mcp_server" {
  name = "mcp_server"
  key  = "mcp_server"
  
  actions = {
    "greet" = { name = "greet" }
    "add"   = { name = "add" }
  }
}

resource "permitio_resource" "mcp_server_tools" {
  name = "mcp_server_tools"
  key  = "mcp_server_tools"
  
  actions = {
    "list" = { name = "list" }
  }
}

# Roles
resource "permitio_role" "Admin" {
  key         = "Admin"
  name        = "Admin"
  permissions = [
    "mcp_server:greet",
    "mcp_server:add", 
    "mcp_server_tools:list"
  ]
}
```

You can also use the [Permit.io CLI](https://github.com/permitio/permit-cli), [API](https://api.permit.io/scalar) or [SDKs](https://github.com/permitio/permit-python) to manage policies, as well as writing policies directly in REGO (Open Policy Agent's policy language).

For complete policy examples including ABAC and RBAC configurations, see [Example Policies](https://github.com/permitio/permit-fastmcp/tree/main/docs/example_policies).

### Identity Management

The middleware supports multiple identity extraction modes:

* **Fixed Identity**: Use a fixed identity for all requests
* **Header-based**: Extract identity from HTTP headers
* **JWT-based**: Extract and verify JWT tokens
* **Source-based**: Use the MCP context source field

For detailed identity mode configuration and environment variables, see [Identity Modes & Environment Variables](https://github.com/permitio/permit-fastmcp/blob/main/docs/identity-modes.md).

#### JWT Authentication Example

```python
import os

# Configure JWT identity extraction
os.environ["PERMIT_MCP_IDENTITY_MODE"] = "jwt"
os.environ["PERMIT_MCP_IDENTITY_JWT_SECRET"] = "your-jwt-secret"

mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))
```

### ABAC Policies with Tool Arguments

The middleware supports Attribute-Based Access Control (ABAC) policies that can evaluate tool arguments as attributes. Tool arguments are automatically flattened as individual attributes (e.g., `arg_name`, `arg_number`) for granular policy conditions.

![ABAC Condition Example](https://mintlify.s3.us-west-1.amazonaws.com/fastmcp/integrations/images/abac_condition_example.png)

*Example: Create dynamic resources with conditions like `resource.arg_number greater-than 10` to allow the `conditional-greet` tool only when the number argument exceeds 10.*

#### Example: Conditional Access

Create a dynamic resource with conditions like `resource.arg_number greater-than 10` to allow the `conditional-greet` tool only when the number argument exceeds 10.

```python
@mcp.tool
def conditional_greet(name: str, number: int) -> str:
    """Greet a user only if number > 10"""
    return f"Hello, {name}! Your number is {number}"
```

![ABAC Policy Example](https://mintlify.s3.us-west-1.amazonaws.com/fastmcp/integrations/images/abac_policy_example.png)

*Example: The Admin role is granted access to the "conditional-greet" action on the "Big-greets" dynamic resource, while other tools like "greet", "greet-jwt", and "login" are granted on the base "mcp\_server" resource.*

For comprehensive ABAC configuration and advanced policy examples, see [ABAC Policies with Tool Arguments](https://github.com/permitio/permit-fastmcp/blob/main/docs/policy-mapping.md#abac-policies-with-tool-arguments).

### Run the Server

Start your FastMCP server normally:

```bash
python server.py
```

The middleware will now intercept all MCP requests and check them against your Permit.io policies. Requests include user identification through the configured identity mode and automatic mapping of MCP methods to authorization resources and actions.

## Advanced Configuration

### Environment Variables

Configure the middleware using environment variables:

```bash
# Permit.io configuration
export PERMIT_MCP_PERMIT_PDP_URL="http://localhost:7766"
export PERMIT_MCP_PERMIT_API_KEY="your-api-key"

# Identity configuration
export PERMIT_MCP_IDENTITY_MODE="jwt"
export PERMIT_MCP_IDENTITY_JWT_SECRET="your-jwt-secret"

# Method configuration
export PERMIT_MCP_KNOWN_METHODS='["tools/list","tools/call"]'
export PERMIT_MCP_BYPASSED_METHODS='["initialize","ping"]'

# Logging configuration
export PERMIT_MCP_ENABLE_AUDIT_LOGGING="true"
```

For a complete list of all configuration options and environment variables, see [Configuration Reference](https://github.com/permitio/permit-fastmcp/blob/main/docs/configuration-reference.md).

### Custom Middleware Configuration

```python
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware

middleware = PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-api-key",
    enable_audit_logging=True,
    bypass_methods=["initialize", "ping", "health/*"]
)

mcp.add_middleware(middleware)
```

For advanced configuration options and custom middleware extensions, see [Advanced Configuration](https://github.com/permitio/permit-fastmcp/blob/main/docs/advanced-configuration.md).

## Example: Complete JWT Authentication Server

See the [example server](https://github.com/permitio/permit-fastmcp/blob/main/permit_fastmcp/example_server/example.py) for a full implementation with JWT-based authentication. For additional examples and usage patterns, see [Example Server](https://github.com/permitio/permit-fastmcp/blob/main/permit_fastmcp/example_server/):

```python
from fastmcp import FastMCP, Context
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware
import jwt
import datetime

# Configure JWT identity extraction
os.environ["PERMIT_MCP_IDENTITY_MODE"] = "jwt"
os.environ["PERMIT_MCP_IDENTITY_JWT_SECRET"] = "mysecretkey"

mcp = FastMCP("My MCP Server")

@mcp.tool
def login(username: str, password: str) -> str:
    """Login to get a JWT token"""
    if username == "admin" and password == "password":
        token = jwt.encode(
            {"sub": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            "mysecretkey",
            algorithm="HS256"
        )
        return f"Bearer {token}"
    raise Exception("Invalid credentials")

@mcp.tool
def greet_jwt(ctx: Context) -> str:
    """Greet a user by extracting their name from JWT"""
    # JWT extraction handled by middleware
    return "Hello, authenticated user!"

mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))

if __name__ == "__main__":
    mcp.run(transport="http")
```

<Tip>
  For detailed policy configuration, custom authentication, and advanced
  deployment patterns, visit the [Permit.io FastMCP Middleware
  repository][permit-fastmcp-github]. For troubleshooting common issues, see [Troubleshooting](https://github.com/permitio/permit-fastmcp/blob/main/docs/troubleshooting.md).
</Tip>

[permit.io]: https://www.permit.io

[permit-github]: https://github.com/permitio

[permit-fastmcp-github]: https://github.com/permitio/permit-fastmcp

[Agent.Security]: https://agent.security

[fastmcp-middleware]: /servers/middleware


# Starlette / ASGI 🤝 FastMCP
Source: https://gofastmcp.com/integrations/starlette

Integrate FastMCP servers into ASGI applications

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.3.1" />

FastMCP servers can be integrated into existing ASGI applications, allowing you to add MCP functionality to your web applications. This is useful for:

* Adding MCP functionality to an existing website or API
* Mounting MCP servers under specific URL paths
* Combining multiple services in a single application
* Leveraging existing authentication and middleware

## Basic Usage

To integrate a FastMCP server into an ASGI application, use the `http_app()` method to obtain a Starlette application instance:

<Tip>
  The `http_app()` method is new in FastMCP 2.3.2. In older versions, use `sse_app()` for SSE transport or `streamable_http_app()` for Streamable HTTP transport.
</Tip>

```python
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

# Get a Starlette app instance for Streamable HTTP transport (recommended)
http_app = mcp.http_app()

# For legacy SSE transport (deprecated)
sse_app = mcp.http_app(transport="sse")
```

The returned Starlette application can be integrated with other ASGI-compatible web frameworks. The MCP server's endpoint is mounted at `/mcp/` for Streamable HTTP transport and `/sse/` for SSE transport.

### Configuration Options

You can customize the endpoint path and access the FastMCP server instance:

```python
# Custom endpoint path
http_app = mcp.http_app(path="/custom-mcp-path")

# Access the FastMCP server from middleware/routes
# The server is available at: request.app.state.fastmcp_server
```

### Adding Custom Routes

You can add custom web routes directly to your FastMCP server using the `@custom_route` decorator:

```python
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/api/status", methods=["GET"])
async def get_status(request: Request):
    return JSONResponse({"server": "running"})

http_app = mcp.http_app()
```

#### Health Check Endpoints

Health checks are commonly needed for monitoring and load balancing:

```python
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})

http_app = mcp.http_app()
```

The health endpoint will be available at `/health` alongside your MCP endpoint at `/mcp/`.

## Starlette Integration

Mount your FastMCP server in another Starlette application:

```python
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

# Create your FastMCP server
mcp = FastMCP("MyServer")

@mcp.tool
def analyze(data: str) -> dict:
    return {"result": f"Analyzed: {data}"}

# Create the ASGI app
mcp_app = mcp.http_app(path='/mcp')

# Create a Starlette app and mount the MCP server
app = Starlette(
    routes=[
        Mount("/mcp-server", app=mcp_app),
        # Add other routes as needed
    ],
    lifespan=mcp_app.lifespan,
)
```

The MCP endpoint will be available at `/mcp-server/mcp/` of the resulting Starlette app.

<Warning>
  For Streamable HTTP transport, you **must** pass the lifespan context from the FastMCP app to the resulting Starlette app, as nested lifespans are not recognized. Otherwise, the FastMCP server's session manager will not be properly initialized.
</Warning>

### Nested Mounts

You can create complex routing structures by nesting mounts:

```python
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

# Create your FastMCP server
mcp = FastMCP("MyServer")

# Create the ASGI app
mcp_app = mcp.http_app(path='/mcp')

# Create nested application structure
inner_app = Starlette(routes=[Mount("/inner", app=mcp_app)])
app = Starlette(
    routes=[Mount("/outer", app=inner_app)],
    lifespan=mcp_app.lifespan,
)
```

In this setup, the MCP server is accessible at the `/outer/inner/mcp/` path.

## Custom Middleware

<VersionBadge version="2.3.2" />

Add custom Starlette middleware to your FastMCP ASGI apps by passing a list of middleware instances:

```python
from fastmcp import FastMCP
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# Create your FastMCP server
mcp = FastMCP("MyServer")

# Define custom middleware
custom_middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

# Create ASGI app with middleware
http_app = mcp.http_app(custom_middleware=custom_middleware)
```

## Running the Server

To run your ASGI application, use an ASGI server like `uvicorn`:

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Or from the command line:

```bash
uvicorn path.to.your.app:app --host 0.0.0.0 --port 8000
```

## Framework-Specific Integration

### FastAPI

For FastAPI-specific integration patterns including both mounting MCP servers into FastAPI apps and generating MCP servers from FastAPI apps, see the [FastAPI Integration guide](/integrations/fastapi).

### Other ASGI Frameworks

The patterns shown here work with any ASGI-compatible framework. The key requirements are:

1. Mount the FastMCP ASGI app at your desired path
2. Pass the lifespan context to your root application
3. Configure any necessary middleware or authentication


# FastMCP CLI
Source: https://gofastmcp.com/patterns/cli

Learn how to use the FastMCP command-line interface

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

FastMCP provides a command-line interface (CLI) that makes it easy to run, develop, and install your MCP servers. The CLI is automatically installed when you install FastMCP.

```bash
fastmcp --help
```

## Commands Overview

| Command   | Purpose                                         | Dependency Management                                                                                                                         |
| --------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `run`     | Run a FastMCP server directly                   | Default: Uses your local environment directly. With `--python`, `--with`, `--project`, or `--with-requirements`: Runs via `uv run` subprocess |
| `dev`     | Run a server with the MCP Inspector for testing | Always runs via `uv run` subprocess (never uses your local environment); dependencies must be specified or available in a uv-managed project  |
| `install` | Install a server in MCP client applications     | Creates an isolated environment; dependencies must be explicitly specified with `--with` and/or `--with-editable`                             |
| `inspect` | Generate a JSON report about a FastMCP server   | Uses your current environment; you are responsible for ensuring all dependencies are available                                                |
| `version` | Display version information                     | N/A                                                                                                                                           |

## Command Details

### `run`

Run a FastMCP server directly or proxy a remote server.

```bash
fastmcp run server.py
```

<Tip>
  By default, this command runs the server directly in your current Python environment. You are responsible for ensuring all dependencies are available. When using `--python`, `--with`, `--project`, or `--with-requirements` options, it runs the server via `uv run` subprocess instead.
</Tip>

#### Options

| Option              | Flag                  | Description                                                                     |
| ------------------- | --------------------- | ------------------------------------------------------------------------------- |
| Transport           | `--transport`, `-t`   | Transport protocol to use (`stdio`, `http`, or `sse`)                           |
| Host                | `--host`              | Host to bind to when using http transport (default: 127.0.0.1)                  |
| Port                | `--port`, `-p`        | Port to bind to when using http transport (default: 8000)                       |
| Path                | `--path`              | Path to bind to when using http transport (default: `/mcp/` or `/sse/` for SSE) |
| Log Level           | `--log-level`, `-l`   | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)                               |
| No Banner           | `--no-banner`         | Disable the startup banner display                                              |
| Python Version      | `--python`            | Python version to use (e.g., 3.10, 3.11)                                        |
| Additional Packages | `--with`              | Additional packages to install (can be used multiple times)                     |
| Project Directory   | `--project`           | Run the command within the given project directory                              |
| Requirements File   | `--with-requirements` | Requirements file to install dependencies from                                  |

#### Server Specification

<VersionBadge version="2.3.5" />

The server can be specified in four ways:

1. `server.py` - imports the module and looks for a FastMCP object named `mcp`, `server`, or `app`. Errors if no such object is found.
2. `server.py:custom_name` - imports and uses the specified server object
3. `http://server-url/path` or `https://server-url/path` - connects to a remote server and creates a proxy
4. `mcp.json` - runs servers defined in a standard MCP configuration file

<Tip>
  When using `fastmcp run` with a local file, it **ignores** the `if __name__ == "__main__"` block entirely. Instead, it finds your server object and calls its `run()` method directly with the transport options you specify. This means you can use `fastmcp run` to override the transport specified in your code.
</Tip>

For example, if your code contains:

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This is ignored when using `fastmcp run`!
    mcp.run(transport="stdio")
```

You can run it with Streamable HTTP transport regardless of what's in the `__main__` block:

```bash
fastmcp run server.py --transport http --port 8000
```

**Examples**

```bash
# Run a local server with Streamable HTTP transport on a custom port
fastmcp run server.py --transport http --port 8000

# Connect to a remote server and proxy as a stdio server
fastmcp run https://example.com/mcp-server

# Connect to a remote server with specified log level
fastmcp run https://example.com/mcp-server --log-level DEBUG

# Run with a specific Python version
fastmcp run server.py --python 3.11

# Run with additional packages
fastmcp run server.py --with pandas --with numpy

# Run within a specific project directory
fastmcp run server.py --project /path/to/project

# Run with dependencies from a requirements file
fastmcp run server.py --with-requirements requirements.txt
```

#### Running MCP Configuration Files

FastMCP can run servers defined in standard MCP configuration files (typically named `mcp.json`). When you run an mcp.json file, FastMCP creates a proxy server that runs all the servers referenced in the configuration.

**Example mcp.json:**

```json
{
    "mcpServers": {
        "fetch": {
            "command": "uvx",
            "args": [
                "mcp-server-fetch"
            ]
        },
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "/Users/username/Documents"
            ]
        }
    }
}
```

**Run the configuration:**

```bash
# Run with default stdio transport
fastmcp run mcp.json

# Run with HTTP transport on custom port
fastmcp run mcp.json --transport http --port 8080

# Run with SSE transport
fastmcp run mcp.json --transport sse
```

### `dev`

Run a MCP server with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) for testing.

```bash
fastmcp dev server.py
```

<Tip>
  This command always runs your server via `uv run` subprocess (never your local environment) to work with the MCP Inspector. All dependencies must be explicitly specified using the `--with` and/or `--with-editable` options, or be available in a uv-managed project.
</Tip>

<Warning>
  The `dev` command is a shortcut for testing a server over STDIO only. When the Inspector launches, you may need to:

  1. Select "STDIO" from the transport dropdown
  2. Connect manually

  This command does not support HTTP testing. To test a server over Streamable HTTP or SSE:

  1. Start your server manually with the appropriate transport using either the command line:
     ```bash
     fastmcp run server.py --transport http
     ```
     or by setting the transport in your code:
     ```bash
     python server.py  # Assuming your __main__ block sets Streamable HTTP transport
     ```
  2. Open the MCP Inspector separately and connect to your running server
</Warning>

#### Options

| Option              | Flag                    | Description                                                     |
| ------------------- | ----------------------- | --------------------------------------------------------------- |
| Editable Package    | `--with-editable`, `-e` | Directory containing pyproject.toml to install in editable mode |
| Additional Packages | `--with`                | Additional packages to install (can be used multiple times)     |
| Inspector Version   | `--inspector-version`   | Version of the MCP Inspector to use                             |
| UI Port             | `--ui-port`             | Port for the MCP Inspector UI                                   |
| Server Port         | `--server-port`         | Port for the MCP Inspector Proxy server                         |
| Python Version      | `--python`              | Python version to use (e.g., 3.10, 3.11)                        |
| Project Directory   | `--project`             | Run the command within the given project directory              |
| Requirements File   | `--with-requirements`   | Requirements file to install dependencies from                  |

**Examples**

```bash
# Run dev server with editable mode and additional packages
fastmcp dev server.py -e . --with pandas --with matplotlib

# Run dev server with specific Python version
fastmcp dev server.py --python 3.11

# Run dev server with requirements file
fastmcp dev server.py --with-requirements requirements.txt

# Run dev server within a specific project directory
fastmcp dev server.py --project /path/to/project
```

### `install`

<VersionBadge version="2.10.3" />

Install a MCP server in MCP client applications. FastMCP currently supports the following clients:

* **Claude Code** - Installs via Claude Code's built-in MCP management system
* **Claude Desktop** - Installs via direct configuration file modification
* **Cursor** - Installs via deeplink that opens Cursor for user confirmation
* **MCP JSON** - Generates standard MCP JSON configuration for manual use

```bash
fastmcp install claude-code server.py
fastmcp install claude-desktop server.py
fastmcp install cursor server.py
fastmcp install mcp-json server.py
```

Note that for security reasons, MCP clients usually run every server in a completely isolated environment. Therefore, all dependencies must be explicitly specified using the `--with` and/or `--with-editable` options (following `uv` conventions) or by attaching them to your server in code via the `dependencies` parameter. You should not assume that the MCP server will have access to your local environment.

<Warning>
  **`uv` must be installed and available in your system PATH**. Both Claude Desktop and Cursor run in isolated environments and need `uv` to manage dependencies. On macOS, install `uv` globally with Homebrew for Claude Desktop compatibility: `brew install uv`.
</Warning>

<Note>
  **Python Version Considerations**: The install commands now support the `--python` option to specify a Python version directly. You can also use `--project` to run within a specific project directory or `--with-requirements` to install dependencies from a requirements file.
</Note>

<Tip>
  **FastMCP `install` commands focus on local server files with STDIO transport.** For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's value is simplifying the complex local setup with dependencies and `uv` commands.
</Tip>

#### Server Specification

The `install` command supports the same `file.py:object` notation as the `run` command:

1. `server.py` - imports the module and looks for a FastMCP object named `mcp`, `server`, or `app`. Errors if no such object is found.
2. `server.py:custom_name` - imports and uses the specified server object

#### Options

| Option                | Flag                    | Description                                                                   |
| --------------------- | ----------------------- | ----------------------------------------------------------------------------- |
| Server Name           | `--server-name`, `-n`   | Custom name for the server (defaults to server's name attribute or file name) |
| Editable Package      | `--with-editable`, `-e` | Directory containing pyproject.toml to install in editable mode               |
| Additional Packages   | `--with`                | Additional packages to install (can be used multiple times)                   |
| Environment Variables | `--env`                 | Environment variables in KEY=VALUE format (can be used multiple times)        |
| Environment File      | `--env-file`, `-f`      | Load environment variables from a .env file                                   |
| Python Version        | `--python`              | Python version to use (e.g., 3.10, 3.11)                                      |
| Project Directory     | `--project`             | Run the command within the given project directory                            |
| Requirements File     | `--with-requirements`   | Requirements file to install dependencies from                                |

**Examples**

```bash
# Auto-detects server object (looks for 'mcp', 'server', or 'app')
fastmcp install claude-desktop server.py

# Uses specific server object
fastmcp install claude-desktop server.py:my_server

# With custom name and dependencies
fastmcp install claude-desktop server.py:my_server --server-name "My Analysis Server" --with pandas

# Install in Claude Code with environment variables
fastmcp install claude-code server.py --env API_KEY=secret --env DEBUG=true

# Install in Cursor with environment variables
fastmcp install cursor server.py --env API_KEY=secret --env DEBUG=true

# Install with environment file
fastmcp install cursor server.py --env-file .env

# Install with specific Python version
fastmcp install claude-desktop server.py --python 3.11

# Install with requirements file
fastmcp install claude-code server.py --with-requirements requirements.txt

# Install within a project directory
fastmcp install cursor server.py --project /path/to/project

# Generate MCP JSON configuration
fastmcp install mcp-json server.py --name "My Server" --with pandas

# Copy JSON configuration to clipboard
fastmcp install mcp-json server.py --copy
```

#### MCP JSON Generation

The `mcp-json` subcommand generates standard MCP JSON configuration that can be used with any MCP-compatible client. This is useful when:

* Working with MCP clients not directly supported by FastMCP
* Creating configuration for CI/CD environments
* Sharing server configurations with others
* Integration with custom tooling

The generated JSON follows the standard MCP server configuration format used by Claude Desktop, VS Code, Cursor, and other MCP clients, with the server name as the root key:

```json
{
  "server-name": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "/path/to/server.py"
    ],
    "env": {
      "API_KEY": "value"
    }
  }
}
```

<Note>
  To use this configuration with your MCP client, you'll typically need to add it to the client's `mcpServers` object. Consult your client's documentation for any specific configuration requirements or formatting needs.
</Note>

**Options specific to mcp-json:**

| Option            | Flag     | Description                                                   |
| ----------------- | -------- | ------------------------------------------------------------- |
| Copy to Clipboard | `--copy` | Copy configuration to clipboard instead of printing to stdout |

### `inspect`

<VersionBadge version="2.9.0" />

Generate a detailed JSON report about a FastMCP server, including information about its tools, prompts, resources, and capabilities.

```bash
fastmcp inspect server.py
```

The command supports the same server specification format as `run` and `install`:

```bash
# Auto-detect server object
fastmcp inspect server.py

# Specify server object
fastmcp inspect server.py:my_server

# Custom output location
fastmcp inspect server.py --output analysis.json
```

### `version`

Display version information about FastMCP and related components.

```bash
fastmcp version
```

#### Options

| Option            | Flag     | Description                           |
| ----------------- | -------- | ------------------------------------- |
| Copy to Clipboard | `--copy` | Copy version information to clipboard |


# Contrib Modules
Source: https://gofastmcp.com/patterns/contrib

Community-contributed modules extending FastMCP

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.2.1" />

FastMCP includes a `contrib` package that holds community-contributed modules. These modules extend FastMCP's functionality but aren't officially maintained by the core team.

Contrib modules provide additional features, integrations, or patterns that complement the core FastMCP library. They offer a way for the community to share useful extensions while keeping the core library focused and maintainable.

The available modules can be viewed in the [contrib directory](https://github.com/jlowin/fastmcp/tree/main/src/fastmcp/contrib).

## Usage

To use a contrib module, import it from the `fastmcp.contrib` package:

```python
from fastmcp.contrib import my_module
```

## Important Considerations

* **Stability**: Modules in `contrib` may have different testing requirements or stability guarantees compared to the core library.
* **Compatibility**: Changes to core FastMCP might break modules in `contrib` without explicit warnings in the main changelog.
* **Dependencies**: Contrib modules may have additional dependencies not required by the core library. These dependencies are typically documented in the module's README or separate requirements files.

## Contributing

We welcome contributions to the `contrib` package! If you have a module that extends FastMCP in a useful way, consider contributing it:

1. Create a new directory in `src/fastmcp/contrib/` for your module
2. Add proper tests for your module in `tests/contrib/`
3. Include comprehensive documentation in a README.md file, including usage and examples, as well as any additional dependencies or installation instructions
4. Submit a pull request

The ideal contrib module:

* Solves a specific use case or integration need
* Follows FastMCP coding standards
* Includes thorough documentation and examples
* Has comprehensive tests
* Specifies any additional dependencies


# Decorating Methods
Source: https://gofastmcp.com/patterns/decorating-methods

Properly use instance methods, class methods, and static methods with FastMCP decorators.

FastMCP's decorator system is designed to work with functions, but you may see unexpected behavior if you try to decorate an instance or class method. This guide explains the correct approach for using methods with all FastMCP decorators (`@tool`, `@resource`, and `.prompt`).

## Why Are Methods Hard?

When you apply a FastMCP decorator like `@tool`, `@resource`, or `@prompt` to a method, the decorator captures the function at decoration time. For instance methods and class methods, this poses a challenge because:

1. For instance methods: The decorator gets the unbound method before any instance exists
2. For class methods: The decorator gets the function before it's bound to the class

This means directly decorating these methods doesn't work as expected. In practice, the LLM would see parameters like `self` or `cls` that it cannot provide values for.

Additionally, **FastMCP decorators return objects (Tool, Resource, or Prompt instances) rather than the original function**. This means that when you decorate a method directly, the method becomes the returned object and is no longer callable by your code:

<Warning>
  **Don't do this!**

  The method will no longer be callable from Python, and the tool won't be callable by LLMs.

  ```python

  from fastmcp import FastMCP
  mcp = FastMCP()

  class MyClass:
      @mcp.tool
      def my_method(self, x: int) -> int:
          return x * 2

  obj = MyClass()
  obj.my_method(5)  # Fails - my_method is a Tool, not a function
  ```
</Warning>

This is another important reason to register methods functionally after defining the class.

## Recommended Patterns

### Instance Methods

<Warning>
  **Don't do this!**

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      @mcp.tool  # This won't work correctly
      def add(self, x, y):
          return x + y
  ```
</Warning>

When the decorator is applied this way, it captures the unbound method. When the LLM later tries to use this component, it will see `self` as a required parameter, but it won't know what to provide for it, causing errors or unexpected behavior.

<Check>
  **Do this instead**:

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      def add(self, x, y):
          return x + y

  # Create an instance first, then register the bound methods
  obj = MyClass()
  mcp.tool(obj.add)

  # Now you can call it without 'self' showing up as a parameter
  await mcp._mcp_call_tool('add', {'x': 1, 'y': 2})  # Returns 3
  ```
</Check>

This approach works because:

1. You first create an instance of the class (`obj`)
2. When you access the method through the instance (`obj.add`), Python creates a bound method where `self` is already set to that instance
3. When you register this bound method, the system sees a callable that only expects the appropriate parameters, not `self`

### Class Methods

The behavior of decorating class methods depends on the order of decorators:

<Warning>
  **Don't do this** (decorator order matters):

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      @classmethod
      @mcp.tool  # This won't work but won't raise an error
      def from_string_v1(cls, s):
          return cls(s)
      
      @mcp.tool
      @classmethod  # This will raise a helpful ValueError
      def from_string_v2(cls, s):
          return cls(s)
  ```
</Warning>

* If `@classmethod` comes first, then `@mcp.tool`: No error is raised, but it won't work correctly
* If `@mcp.tool` comes first, then `@classmethod`: FastMCP will detect this and raise a helpful `ValueError` with guidance

<Check>
  **Do this instead**:

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      @classmethod
      def from_string(cls, s):
          return cls(s)

  # Register the class method after the class is defined
  mcp.tool(MyClass.from_string)
  ```
</Check>

This works because:

1. The `@classmethod` decorator is applied properly during class definition
2. When you access `MyClass.from_string`, Python provides a special method object that automatically binds the class to the `cls` parameter
3. When registered, only the appropriate parameters are exposed to the LLM, hiding the implementation detail of the `cls` parameter

### Static Methods

Static methods "work" with FastMCP decorators, but this is not recommended because the FastMCP decorator will not return a callable method. Therefore, you should register static methods the same way as other methods.

<Warning>
  **This is not recommended, though it will work.**

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      @mcp.tool
      @staticmethod
      def utility(x, y):
          return x + y
  ```
</Warning>

This works because `@staticmethod` converts the method to a regular function, which the FastMCP decorator can then properly process. However, this is not recommended because the FastMCP decorator will not return a callable staticmethod. Therefore, you should register static methods the same way as other methods.

<Check>
  **Prefer this pattern:**

  ```python
  from fastmcp import FastMCP

  mcp = FastMCP()

  class MyClass:
      @staticmethod
      def utility(x, y):
          return x + y

  # This also works
  mcp.tool(MyClass.utility)
  ```
</Check>

## Additional Patterns

### Creating Components at Class Initialization

You can automatically register instance methods when creating an object:

```python
from fastmcp import FastMCP

mcp = FastMCP()

class ComponentProvider:
    def __init__(self, mcp_instance):
        # Register methods
        mcp_instance.tool(self.tool_method)
        mcp_instance.resource("resource://data")(self.resource_method)
    
    def tool_method(self, x):
        return x * 2
    
    def resource_method(self):
        return "Resource data"

# The methods are automatically registered when creating the instance
provider = ComponentProvider(mcp)
```

This pattern is useful when:

* You want to encapsulate registration logic within the class itself
* You have multiple related components that should be registered together
* You want to ensure that methods are always properly registered when creating an instance

The class automatically registers its methods during initialization, ensuring they're properly bound to the instance before registration.

## Summary

The current behavior of FastMCP decorators with methods is:

* **Static methods**: Can be decorated directly and work perfectly with all FastMCP decorators
* **Class methods**: Cannot be decorated directly and will raise a helpful `ValueError` with guidance
* **Instance methods**: Should be registered after creating an instance using the decorator calls

For class and instance methods, you should register them after creating the instance or class to ensure proper method binding. This ensures that the methods are properly bound before being registered.

Understanding these patterns allows you to effectively organize your components into classes while maintaining proper method binding, giving you the benefits of object-oriented design without sacrificing the simplicity of FastMCP's decorator system.


# HTTP Requests
Source: https://gofastmcp.com/patterns/http-requests

Accessing and using HTTP requests in FastMCP servers

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.2.11" />

## Overview

When running FastMCP as a web server, your MCP tools, resources, and prompts might need to access the underlying HTTP request information, such as headers, client IP, or query parameters.

FastMCP provides a clean way to access HTTP request information through a dependency function.

## Accessing HTTP Requests

The recommended way to access the current HTTP request is through the `get_http_request()` dependency function:

```python {2, 3, 11}
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

mcp = FastMCP(name="HTTP Request Demo")

@mcp.tool
async def user_agent_info() -> dict:
    """Return information about the user agent."""
    # Get the HTTP request
    request: Request = get_http_request()
    
    # Access request data
    user_agent = request.headers.get("user-agent", "Unknown")
    client_ip = request.client.host if request.client else "Unknown"
    
    return {
        "user_agent": user_agent,
        "client_ip": client_ip,
        "path": request.url.path,
    }
```

This approach works anywhere within a request's execution flow, not just within your MCP function. It's useful when:

1. You need access to HTTP information in helper functions
2. You're calling nested functions that need HTTP request data
3. You're working with middleware or other request processing code

## Accessing HTTP Headers Only

If you only need request headers and want to avoid potential errors, you can use the `get_http_headers()` helper:

```python {2}
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

mcp = FastMCP(name="Headers Demo")

@mcp.tool
async def safe_header_info() -> dict:
    """Safely get header information without raising errors."""
    # Get headers (returns empty dict if no request context)
    headers = get_http_headers()
    
    # Get authorization header
    auth_header = headers.get("authorization", "")
    is_bearer = auth_header.startswith("Bearer ")
    
    return {
        "user_agent": headers.get("user-agent", "Unknown"),
        "content_type": headers.get("content-type", "Unknown"),
        "has_auth": bool(auth_header),
        "auth_type": "Bearer" if is_bearer else "Other" if auth_header else "None",
        "headers_count": len(headers)
    }
```

By default, `get_http_headers()` excludes problematic headers like `host` and `content-length`. To include all headers, use `get_http_headers(include_all=True)`.

## Important Notes

* HTTP requests are only available when FastMCP is running as part of a web application
* Accessing the HTTP request with `get_http_request()` outside of a web request context will raise a `RuntimeError`
* The `get_http_headers()` function **never raises errors** - it returns an empty dict when no request context is available
* The `get_http_request()` function returns a standard [Starlette Request](https://www.starlette.io/requests/) object


# Testing MCP Servers
Source: https://gofastmcp.com/patterns/testing

Learn how to test your FastMCP servers effectively

Testing your MCP servers thoroughly is essential for ensuring they work correctly when deployed. FastMCP makes this easy through a variety of testing patterns.

## In-Memory Testing

The most efficient way to test an MCP server is to pass your FastMCP server instance directly to a Client. This enables in-memory testing without having to start a separate server process, which is particularly useful because managing an MCP server programmatically can be challenging.

Here is an example of using a `Client` to test a server with pytest:

```python
import pytest
from fastmcp import FastMCP, Client

@pytest.fixture
def mcp_server():
    server = FastMCP("TestServer")
    
    @server.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"
        
    return server

async def test_tool_functionality(mcp_server):
    # Pass the server directly to the Client constructor
    async with Client(mcp_server) as client:
        result = await client.call_tool("greet", {"name": "World"})
        assert result.data == "Hello, World!"
```

This pattern creates a direct connection between the client and server, allowing you to test your server's functionality efficiently.

<Tip>
  If you're using pytest for async tests, as shown above, you may need to configure appropriate markers or set `asyncio_mode = "auto"` in your pytest configuration in order to handle async test functions automatically.
</Tip>

## Mocking

FastMCP servers are designed to work seamlessly with standard Python testing tools and patterns. There's nothing special about testing FastMCP servers - you can use all the familiar Python mocking, patching, and testing techniques you already know.


# Tool Transformation
Source: https://gofastmcp.com/patterns/tool-transformation

Create enhanced tool variants with modified schemas, argument mappings, and custom behavior.

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.8.0" />

Tool transformation allows you to create new, enhanced tools from existing ones. This powerful feature enables you to adapt tools for different contexts, simplify complex interfaces, or add custom logic without duplicating code.

## Why Transform Tools?

Often, an existing tool is *almost* perfect for your use case, but it might have:

* A confusing description (or no description at all).
* Argument names or descriptions that are not intuitive for an LLM (e.g., `q` instead of `query`).
* Unnecessary parameters that you want to hide from the LLM.
* A need for input validation before the original tool is called.
* A need to modify or format the tool's output.

Instead of rewriting the tool from scratch, you can **transform** it to fit your needs.

## Basic Transformation

The primary way to create a transformed tool is with the `Tool.from_tool()` class method. At its simplest, you can use it to change a tool's top-level metadata like its `name`, `description`, or `tags`.

In the following simple example, we take a generic `search` tool and adjust its name and description to help an LLM client better understand its purpose.

```python {13-21}
from fastmcp import FastMCP
from fastmcp.tools import Tool

mcp = FastMCP()

# The original, generic tool
@mcp.tool
def search(query: str, category: str = "all") -> list[dict]:
    """Searches for items in the database."""
    return database.search(query, category)

# Create a more domain-specific version by changing its metadata
product_search_tool = Tool.from_tool(
    search,
    name="find_products",
    description="""
        Search for products in the e-commerce catalog. 
        Use this when customers ask about finding specific items, 
        checking availability, or browsing product categories.
        """,
)

mcp.add_tool(product_search_tool)
```

<Tip>
  When you transform a tool, the original tool remains registered on the server. To avoid confusing an LLM with two similar tools, you can disable the original one:

  ```python
  from fastmcp import FastMCP
  from fastmcp.tools import Tool

  mcp = FastMCP()

  # The original, generic tool
  @mcp.tool
  def search(query: str, category: str = "all") -> list[dict]:
      ...

  # Create a more domain-specific version
  product_search_tool = Tool.from_tool(search, ...)
  mcp.add_tool(product_search_tool)

  # Disable the original tool
  search.disable()
  ```
</Tip>

Now, clients see a tool named `find_products` with a clear, domain-specific purpose and relevant tags, even though it still uses the original generic `search` function's logic.

### Parameters

The `Tool.from_tool()` class method is the primary way to create a transformed tool. It takes the following parameters:

* `tool`: The tool to transform. This is the only required argument.
* `name`: An optional name for the new tool.
* `description`: An optional description for the new tool.
* `transform_args`: A dictionary of `ArgTransform` objects, one for each argument you want to modify.
* `transform_fn`: An optional function that will be called instead of the parent tool's logic.
* `output_schema`: Control output schema and structured outputs (see [Output Schema Control](#output-schema-control)).
* `tags`: An optional set of tags for the new tool.
* `annotations`: An optional set of `ToolAnnotations` for the new tool.
* `serializer`: An optional function that will be called to serialize the result of the new tool.

The result is a new `TransformedTool` object that wraps the parent tool and applies the transformations you specify. You can add this tool to your MCP server using its `add_tool()` method.

## Modifying Arguments

To modify a tool's parameters, provide a dictionary of `ArgTransform` objects to the `transform_args` parameter of `Tool.from_tool()`. Each key is the name of the *original* argument you want to modify.

<Tip>
  You only need to provide a `transform_args` entry for arguments you want to modify. All other arguments will be passed through unchanged.
</Tip>

### The ArgTransform Class

To modify an argument, you need to create an `ArgTransform` object. This object has the following parameters:

* `name`: The new name for the argument.
* `description`: The new description for the argument.
* `default`: The new default value for the argument.
* `default_factory`: A function that will be called to generate a default value for the argument. This is useful for arguments that need to be generated for each tool call, such as timestamps or unique IDs.
* `hide`: Whether to hide the argument from the LLM.
* `required`: Whether the argument is required, usually used to make an optional argument be required instead.
* `type`: The new type for the argument.

<Tip>
  Certain combinations of parameters are not allowed. For example, you can only use `default_factory` with `hide=True`, because dynamic defaults cannot be represented in a JSON schema for the client. You can only set required=True for arguments that do not declare a default value.
</Tip>

### Descriptions

By far the most common reason to transform a tool, after its own description, is to improve its argument descriptions. A good description is crucial for helping an LLM understand how to use a parameter correctly. This is especially important when wrapping tools from external APIs, whose argument descriptions may be missing or written for developers, not LLMs.

In this example, we add a helpful description to the `user_id` argument:

```python {16-19}
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def find_user(user_id: str):
    """Finds a user by their ID."""
    ...

new_tool = Tool.from_tool(
    find_user,
    transform_args={
        "user_id": ArgTransform(
            description=(
                "The unique identifier for the user, "
                "usually in the format 'usr-xxxxxxxx'."
            )
        )
    }
)
```

### Names

At times, you may want to rename an argument to make it more intuitive for an LLM.

For example, in the following example, we take a generic `q` argument and expand it to `search_query`:

```python {15}
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def search(q: str):
    """Searches for items in the database."""
    return database.search(q)

new_tool = Tool.from_tool(
    search,
    transform_args={
        "q": ArgTransform(name="search_query")
    }
)
```

### Default Values

You can update the default value for any argument using the `default` parameter. Here, we change the default value of the `y` argument to 10:

```python{15}
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

new_tool = Tool.from_tool(
    add,
    transform_args={
        "y": ArgTransform(default=10)
    }
)
```

Default values are especially useful in combination with hidden arguments.

### Hiding Arguments

Sometimes a tool requires arguments that shouldn't be exposed to the LLM, such as API keys, configuration flags, or internal IDs. You can hide these parameters using `hide=True`. Note that you can only hide arguments that have a default value (or for which you provide a new default), because the LLM can't provide a value at call time.

<Tip>
  To pass a constant value to the parent tool, combine `hide=True` with `default=<value>`.
</Tip>

```python {19-20}
import os
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def send_email(to: str, subject: str, body: str, api_key: str):
    """Sends an email."""
    ...
    
# Create a simplified version that hides the API key
new_tool = Tool.from_tool(
    send_email,
    name="send_notification",
    transform_args={
        "api_key": ArgTransform(
            hide=True, 
            default=os.environ.get("EMAIL_API_KEY"),
        )
    }
)
```

The LLM now only sees the `to`, `subject`, and `body` parameters. The `api_key` is supplied automatically from an environment variable.

For values that must be generated for each tool call (like timestamps or unique IDs), use `default_factory`, which is called with no arguments every time the tool is called. For example,

```python {3-4}
transform_args = {
    'timestamp': ArgTransform(
        hide=True,
        default_factory=lambda: datetime.now(),
    )
}
```

<Warning>
  `default_factory` can only be used with `hide=True`. This is because visible parameters need static defaults that can be represented in a JSON schema for the client.
</Warning>

### Required Values

In rare cases where you want to make an optional argument required, you can set `required=True`. This has no effect if the argument was already required.

```python {3}
transform_args = {
    'user_id': ArgTransform(
        required=True,
    )
}
```

## Modifying Tool Behavior

<Warning>
  With great power comes great responsibility. Modifying tool behavior is a very advanced feature.
</Warning>

In addition to changing a tool's schema, advanced users can also modify its behavior. This is useful for adding validation logic, or for post-processing the tool's output.

The `from_tool()` method takes a `transform_fn` parameter, which is an async function that replaces the parent tool's logic and gives you complete control over the tool's execution.

### The Transform Function

The `transform_fn` is an async function that **completely replaces** the parent tool's logic.

Critically, the transform function's arguments are used to determine the new tool's final schema. Any arguments that are not already present in the parent tool schema OR the `transform_args` will be added to the new tool's schema. Note that when `transform_args` and your function have the same argument name, the `transform_args` metadata will take precedence, if provided.

```python
async def my_custom_logic(user_input: str, max_length: int = 100) -> str:
    # Your custom logic here - this completely replaces the parent tool
    return f"Custom result for: {user_input[:max_length]}"

Tool.from_tool(transform_fn=my_custom_logic)
```

<Tip>
  The name / docstring of the `transform_fn` are ignored. Only its arguments are used to determine the final schema.
</Tip>

### Calling the Parent Tool

Most of the time, you don't want to completely replace the parent tool's behavior. Instead, you want to add validation, modify inputs, or post-process outputs while still leveraging the parent tool's core functionality. For this, FastMCP provides the special `forward()` and `forward_raw()` functions.

Both `forward()` and `forward_raw()` are async functions that let you call the parent tool from within your `transform_fn`:

* **`forward()`** (recommended): Automatically handles argument mapping based on your `ArgTransform` configurations. Call it with the transformed argument names.
* **`forward_raw()`**: Bypasses all transformation and calls the parent tool directly with its original argument names. This is rarely needed unless you're doing complex argument manipulation, perhaps without `arg_transforms`.

The most common transformation pattern is to validate (potentially renamed) arguments before calling the parent tool. Here's an example that validates that `x` and `y` are positive before calling the parent tool:

<Tabs>
  <Tab title="Using forward()">
    In the simplest case, your parent tool and your transform function have the same arguments. You can call `forward()` with the same argument names as the parent tool:

    ```python {15}
    from fastmcp import FastMCP
    from fastmcp.tools import Tool
    from fastmcp.tools.tool_transform import forward

    mcp = FastMCP()

    @mcp.tool
    def add(x: int, y: int) -> int:
        """Adds two numbers."""
        return x + y

    async def ensure_positive(x: int, y: int) -> int:
        if x <= 0 or y <= 0:
            raise ValueError("x and y must be positive")
        return await forward(x=x, y=y)

    new_tool = Tool.from_tool(
        add,
        transform_fn=ensure_positive,
    )

    mcp.add_tool(new_tool)
    ```
  </Tab>

  <Tab title="Using forward() with renamed args">
    When your transformed tool has different argument names than the parent tool, you can call `forward()` with the renamed arguments and it will automatically map the arguments to the parent tool's arguments:

    ```python {15, 20-23}
    from fastmcp import FastMCP
    from fastmcp.tools import Tool
    from fastmcp.tools.tool_transform import forward

    mcp = FastMCP()

    @mcp.tool
    def add(x: int, y: int) -> int:
        """Adds two numbers."""
        return x + y

    async def ensure_positive(a: int, b: int) -> int:
        if a <= 0 or b <= 0:
            raise ValueError("a and b must be positive")
        return await forward(a=a, b=b)

    new_tool = Tool.from_tool(
        add,
        transform_fn=ensure_positive,
        transform_args={
            "x": ArgTransform(name="a"),
            "y": ArgTransform(name="b"),
        }
    )

    mcp.add_tool(new_tool)
    ```
  </Tab>

  <Tab title="Using forward_raw()">
    Finally, you can use `forward_raw()` to bypass all argument mapping and call the parent tool directly with its original argument names.

    ```python {15, 20-23}
    from fastmcp import FastMCP
    from fastmcp.tools import Tool
    from fastmcp.tools.tool_transform import forward

    mcp = FastMCP()

    @mcp.tool
    def add(x: int, y: int) -> int:
        """Adds two numbers."""
        return x + y

    async def ensure_positive(a: int, b: int) -> int:
        if a <= 0 or b <= 0:
            raise ValueError("a and b must be positive")
        return await forward_raw(x=a, y=b)

    new_tool = Tool.from_tool(
        add,
        transform_fn=ensure_positive,
        transform_args={
            "x": ArgTransform(name="a"),
            "y": ArgTransform(name="b"),
        }
    )

    mcp.add_tool(new_tool)
    ```
  </Tab>
</Tabs>

### Passing Arguments with \*\*kwargs

If your `transform_fn` includes `**kwargs` in its signature, it will receive **all arguments from the parent tool after `ArgTransform` configurations have been applied**. This is powerful for creating flexible validation functions that don't require you to add every argument to the function signature.

In the following example, we wrap a parent tool that accepts two arguments `x` and `y`. These are renamed to `a` and `b` in the transformed tool, and the transform only validates `a`, passing the other argument through as `**kwargs`.

```python {12, 15}
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_a_positive(a: int, **kwargs) -> int:
    if a <= 0:
        raise ValueError("a must be positive")
    return await forward(a=a, **kwargs)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_a_positive,
    transform_args={
        "x": ArgTransform(name="a"),
        "y": ArgTransform(name="b"),
    }
)

mcp.add_tool(new_tool)
```

<Tip>
  In the above example, `**kwargs` receives the renamed argument `b`, not the original argument `y`. It is therefore recommended to use with `forward()`, not `forward_raw()`.
</Tip>

## Modifying MCP Tools with MCPConfig

When running MCP Servers under FastMCP with `MCPConfig`, you can also apply a subset of tool transformations
directly in the MCPConfig json file.

```json
{
    "mcpServers": {
        "weather": {
            "url": "https://weather.example.com/mcp",
            "transport": "http",
            "tools": {
                "weather_get_forecast": {
                    "name": "miami_weather",
                    "description": "Get the weather for Miami",
                    "arguments": {
                        "city": {
                            "name": "city",
                            "default": "Miami",
                            "hide": True,
                        }
                    }
                }
            }
        }
    }
}
```

The `tools` section is a dictionary of tool names to tool configurations. Each tool configuration is a
dictionary of tool properties.

See the [MCPConfigTransport](/clients/transports#tool-transformation-with-fastmcp-and-mcpconfig) documentation for more details.

## Output Schema Control

<VersionBadge version="2.10.0" />

Transformed tools inherit output schemas from their parent by default, but you can control this behavior:

**Inherit from Parent (Default)**

```python
Tool.from_tool(parent_tool, name="renamed_tool")
```

The transformed tool automatically uses the parent tool's output schema and structured output behavior.

**Custom Output Schema**

```python
Tool.from_tool(parent_tool, output_schema={
    "type": "object", 
    "properties": {"status": {"type": "string"}}
})
```

Provide your own schema that differs from the parent. The tool must return data matching this schema.

**Remove Output Schema**

```python
Tool.from_tool(parent_tool, output_schema=False)
```

Removes the output schema declaration. Automatic structured content still works for object-like returns (dict, dataclass, Pydantic models) but primitive types won't be structured.

**Full Control with Transform Functions**

```python
async def custom_output(**kwargs) -> ToolResult:
    result = await forward(**kwargs)
    return ToolResult(content=[...], structured_content={...})

Tool.from_tool(parent_tool, transform_fn=custom_output)
```

Use a transform function returning `ToolResult` for complete control over both content blocks and structured outputs.

## Common Patterns

Tool transformation is a flexible feature that supports many powerful patterns. Here are a few common use cases to give you ideas.

### Adapting Remote or Generated Tools

This is one of the most common reasons to use tool transformation. Tools from remote servers (via a [proxy](/servers/proxy)) or generated from an [OpenAPI spec](/servers/openapi) are often too generic for direct use by an LLM. You can use transformation to create a simpler, more intuitive version for your specific needs.

### Chaining Transformations

You can chain transformations by using an already transformed tool as the parent for a new transformation. This lets you build up complex behaviors in layers, for example, first renaming arguments, and then adding validation logic to the renamed tool.

### Context-Aware Tool Factories

You can write functions that act as "factories," generating specialized versions of a tool for different contexts. For example, you could create a `get_my_data` tool that is specific to the currently logged-in user by hiding the `user_id` parameter and providing it automatically.


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-__init__



# `fastmcp.cli`

FastMCP CLI package.


# claude
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-claude



# `fastmcp.cli.claude`

Claude app integration utilities.

## Functions

### `get_claude_config_path` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/claude.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_claude_config_path() -> Path | None
```

Get the Claude config directory based on platform.

### `update_claude_config` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/claude.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
update_claude_config(file_spec: str, server_name: str) -> bool
```

Add or update a FastMCP server in Claude's configuration.

**Args:**

* `file_spec`: Path to the server file, optionally with :object suffix
* `server_name`: Name for the server in Claude's config
* `with_editable`: Optional directory to install in editable mode
* `with_packages`: Optional list of additional packages to install
* `env_vars`: Optional dictionary of environment variables. These are merged with
  any existing variables, with new values taking precedence.

**Raises:**

* `RuntimeError`: If Claude Desktop's config directory is not found, indicating
  Claude Desktop may not be installed or properly set up.


# cli
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-cli



# `fastmcp.cli.cli`

FastMCP CLI tools using Cyclopts.

## Functions

### `version` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/cli.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
version()
```

Display version information and platform details.

### `dev` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/cli.py#L141" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
dev(server_spec: str) -> None
```

Run an MCP server with the MCP Inspector for development.

**Args:**

* `server_spec`: Python file to run, optionally with :object suffix

### `run` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/cli.py#L286" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
run(server_spec: str) -> None
```

Run an MCP server or connect to a remote one.

The server can be specified in four ways:

1. Module approach: "server.py" - runs the module directly, looking for an object named 'mcp', 'server', or 'app'
2. Import approach: "server.py:app" - imports and runs the specified server object
3. URL approach: "[http://server-url](http://server-url)" - connects to a remote server and creates a proxy
4. MCPConfig file: "mcp.json" - runs as a proxy server for the MCP Servers in the MCPConfig file

Server arguments can be passed after -- :
fastmcp run server.py -- --config config.json --debug

**Args:**

* `server_spec`: Python file, object specification (file:obj), MCPConfig file, or URL

### `inspect` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/cli.py#L442" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
inspect(server_spec: str) -> None
```

Inspect an MCP server and generate a JSON report.

This command analyzes an MCP server and generates a comprehensive JSON report
containing information about the server's name, instructions, version, tools,
prompts, resources, templates, and capabilities.

**Examples:**

fastmcp inspect server.py
fastmcp inspect server.py -o report.json
fastmcp inspect server.py:mcp -o analysis.json
fastmcp inspect path/to/server.py:app -o /tmp/server-info.json

**Args:**

* `server_spec`: Python file to inspect, optionally with :object suffix


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-__init__



# `fastmcp.cli.install`

Install subcommands for FastMCP CLI using Cyclopts.


# claude_code
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-claude_code



# `fastmcp.cli.install.claude_code`

Claude Code integration for FastMCP install using Cyclopts.

## Functions

### `find_claude_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_code.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
find_claude_command() -> str | None
```

Find the Claude Code CLI command.

Checks common installation locations since 'claude' is often a shell alias
that doesn't work with subprocess calls.

### `check_claude_code_available` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_code.py#L67" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
check_claude_code_available() -> bool
```

Check if Claude Code CLI is available.

### `install_claude_code` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_code.py#L72" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
install_claude_code(file: Path, server_object: str | None, name: str) -> bool
```

Install FastMCP server in Claude Code.

**Args:**

* `file`: Path to the server file
* `server_object`: Optional server object name (for :object suffix)
* `name`: Name for the server in Claude Code
* `with_editable`: Optional directory to install in editable mode
* `with_packages`: Optional list of additional packages to install
* `env_vars`: Optional dictionary of environment variables
* `python_version`: Optional Python version to use
* `with_requirements`: Optional requirements file to install from
* `project`: Optional project directory to run within

**Returns:**

* True if installation was successful, False otherwise

### `claude_code_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_code.py#L170" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
claude_code_command(server_spec: str) -> None
```

Install an MCP server in Claude Code.

**Args:**

* `server_spec`: Python file to install, optionally with :object suffix


# claude_desktop
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-claude_desktop



# `fastmcp.cli.install.claude_desktop`

Claude Desktop integration for FastMCP install using Cyclopts.

## Functions

### `get_claude_config_path` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_desktop.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_claude_config_path() -> Path | None
```

Get the Claude config directory based on platform.

### `install_claude_desktop` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_desktop.py#L37" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
install_claude_desktop(file: Path, server_object: str | None, name: str) -> bool
```

Install FastMCP server in Claude Desktop.

**Args:**

* `file`: Path to the server file
* `server_object`: Optional server object name (for :object suffix)
* `name`: Name for the server in Claude's config
* `with_editable`: Optional directory to install in editable mode
* `with_packages`: Optional list of additional packages to install
* `env_vars`: Optional dictionary of environment variables
* `python_version`: Optional Python version to use
* `with_requirements`: Optional requirements file to install from
* `project`: Optional project directory to run within

**Returns:**

* True if installation was successful, False otherwise

### `claude_desktop_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/claude_desktop.py#L143" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
claude_desktop_command(server_spec: str) -> None
```

Install an MCP server in Claude Desktop.

**Args:**

* `server_spec`: Python file to install, optionally with :object suffix


# cursor
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-cursor



# `fastmcp.cli.install.cursor`

Cursor integration for FastMCP install using Cyclopts.

## Functions

### `generate_cursor_deeplink` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/cursor.py#L20" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
generate_cursor_deeplink(server_name: str, server_config: StdioMCPServer) -> str
```

Generate a Cursor deeplink for installing the MCP server.

**Args:**

* `server_name`: Name of the server
* `server_config`: Server configuration

**Returns:**

* Deeplink URL that can be clicked to install the server

### `open_deeplink` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/cursor.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
open_deeplink(deeplink: str) -> bool
```

Attempt to open a deeplink URL using the system's default handler.

**Args:**

* `deeplink`: The deeplink URL to open

**Returns:**

* True if the command succeeded, False otherwise

### `install_cursor` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/cursor.py#L67" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
install_cursor(file: Path, server_object: str | None, name: str) -> bool
```

Install FastMCP server in Cursor.

**Args:**

* `file`: Path to the server file
* `server_object`: Optional server object name (for :object suffix)
* `name`: Name for the server in Cursor
* `with_editable`: Optional directory to install in editable mode
* `with_packages`: Optional list of additional packages to install
* `env_vars`: Optional dictionary of environment variables
* `python_version`: Optional Python version to use
* `with_requirements`: Optional requirements file to install from
* `project`: Optional project directory to run within

**Returns:**

* True if installation was successful, False otherwise

### `cursor_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/cursor.py#L153" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
cursor_command(server_spec: str) -> None
```

Install an MCP server in Cursor.

**Args:**

* `server_spec`: Python file to install, optionally with :object suffix


# mcp_json
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-mcp_json



# `fastmcp.cli.install.mcp_json`

MCP configuration JSON generation for FastMCP install using Cyclopts.

## Functions

### `install_mcp_json` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/mcp_json.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
install_mcp_json(file: Path, server_object: str | None, name: str) -> bool
```

Generate MCP configuration JSON for manual installation.

**Args:**

* `file`: Path to the server file
* `server_object`: Optional server object name (for :object suffix)
* `name`: Name for the server in MCP config
* `with_editable`: Optional directory to install in editable mode
* `with_packages`: Optional list of additional packages to install
* `env_vars`: Optional dictionary of environment variables
* `copy`: If True, copy to clipboard instead of printing to stdout
* `python_version`: Optional Python version to use
* `with_requirements`: Optional requirements file to install from
* `project`: Optional project directory to run within

**Returns:**

* True if generation was successful, False otherwise

### `mcp_json_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/mcp_json.py#L116" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
mcp_json_command(server_spec: str) -> None
```

Generate MCP configuration JSON for manual installation.

**Args:**

* `server_spec`: Python file to install, optionally with :object suffix


# shared
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-install-shared



# `fastmcp.cli.install.shared`

Shared utilities for install commands.

## Functions

### `parse_env_var` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/shared.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
parse_env_var(env_var: str) -> tuple[str, str]
```

Parse environment variable string in format KEY=VALUE.

### `process_common_args` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/install/shared.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
process_common_args(server_spec: str, server_name: str | None, with_packages: list[str], env_vars: list[str], env_file: Path | None) -> tuple[Path, str | None, str, list[str], dict[str, str] | None]
```

Process common arguments shared by all install commands.


# run
Source: https://gofastmcp.com/python-sdk/fastmcp-cli-run



# `fastmcp.cli.run`

FastMCP run command implementation with enhanced type hints.

## Functions

### `is_url` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
is_url(path: str) -> bool
```

Check if a string is a URL.

### `parse_file_path` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L27" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
parse_file_path(server_spec: str) -> tuple[Path, str | None]
```

Parse a file path that may include a server object specification.

**Args:**

* `server_spec`: Path to file, optionally with :object suffix

**Returns:**

* Tuple of (file\_path, server\_object)

### `import_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L58" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
import_server(file: Path, server_object: str | None = None) -> Any
```

Import a MCP server from a file.

**Args:**

* `file`: Path to the file
* `server_object`: Optional object name in format "module:object" or just "object"

**Returns:**

* The server object

### `run_with_uv` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L128" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
run_with_uv(server_spec: str, python_version: str | None = None, with_packages: list[str] | None = None, with_requirements: Path | None = None, project: Path | None = None, transport: TransportType | None = None, host: str | None = None, port: int | None = None, path: str | None = None, log_level: LogLevelType | None = None, show_banner: bool = True) -> None
```

Run a MCP server using uv run subprocess.

**Args:**

* `server_spec`: Python file, object specification (file:obj), or URL
* `python_version`: Python version to use (e.g. "3.10")
* `with_packages`: Additional packages to install
* `with_requirements`: Requirements file to use
* `project`: Run the command within the given project directory
* `transport`: Transport protocol to use
* `host`: Host to bind to when using http transport
* `port`: Port to bind to when using http transport
* `path`: Path to bind to when using http transport
* `log_level`: Log level
* `show_banner`: Whether to show the server banner

### `create_client_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L206" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_client_server(url: str) -> Any
```

Create a FastMCP server from a client URL.

**Args:**

* `url`: The URL to connect to

**Returns:**

* A FastMCP server instance

### `create_mcp_config_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L226" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_mcp_config_server(mcp_config_path: Path) -> FastMCP[None]
```

Create a FastMCP server from a MCPConfig.

### `import_server_with_args` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L237" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
import_server_with_args(file: Path, server_object: str | None = None, server_args: list[str] | None = None) -> Any
```

Import a server with optional command line arguments.

**Args:**

* `file`: Path to the server file
* `server_object`: Optional server object name
* `server_args`: Optional command line arguments to inject

**Returns:**

* The imported server object

### `run_command` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/cli/run.py#L261" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
run_command(server_spec: str, transport: TransportType | None = None, host: str | None = None, port: int | None = None, path: str | None = None, log_level: LogLevelType | None = None, server_args: list[str] | None = None, show_banner: bool = True, use_direct_import: bool = False) -> None
```

Run a MCP server or connect to a remote one.

**Args:**

* `server_spec`: Python file, object specification (file:obj), MCPConfig file, or URL
* `transport`: Transport protocol to use
* `host`: Host to bind to when using http transport
* `port`: Port to bind to when using http transport
* `path`: Path to bind to when using http transport
* `log_level`: Log level
* `server_args`: Additional arguments to pass to the server
* `show_banner`: Whether to show the server banner
* `use_direct_import`: Whether to use direct import instead of subprocess


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-client-__init__



# `fastmcp.client`

*This module is empty or contains only private/internal implementations.*


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-client-auth-__init__



# `fastmcp.client.auth`

*This module is empty or contains only private/internal implementations.*


# bearer
Source: https://gofastmcp.com/python-sdk/fastmcp-client-auth-bearer



# `fastmcp.client.auth.bearer`

## Classes

### `BearerAuth` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/bearer.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `auth_flow` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/bearer.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
auth_flow(self, request)
```


# oauth
Source: https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth



# `fastmcp.client.auth.oauth`

## Functions

### `default_cache_dir` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
default_cache_dir() -> Path
```

### `discover_oauth_metadata` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L153" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
discover_oauth_metadata(server_base_url: str, httpx_kwargs: dict[str, Any] | None = None) -> OAuthMetadata | None
```

Discover OAuth metadata from the server using RFC 8414 well-known endpoint.

**Args:**

* `server_base_url`: Base URL of the OAuth server (e.g., "[https://example.com](https://example.com)")
* `httpx_kwargs`: Additional kwargs for httpx client

**Returns:**

* OAuth metadata if found, None otherwise

### `check_if_auth_required` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L188" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
check_if_auth_required(mcp_url: str, httpx_kwargs: dict[str, Any] | None = None) -> bool
```

Check if the MCP endpoint requires authentication by making a test request.

**Returns:**

* True if auth appears to be required, False otherwise

### `OAuth` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L218" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
OAuth(mcp_url: str, scopes: str | list[str] | None = None, client_name: str = 'FastMCP Client', token_storage_cache_dir: Path | None = None, additional_client_metadata: dict[str, Any] | None = None) -> OAuthClientProvider
```

Create an OAuthClientProvider for an MCP server.

This is intended to be provided to the `auth` parameter of an
httpx.AsyncClient (or appropriate FastMCP client/transport instance)

**Args:**

* `mcp_url`: Full URL to the MCP endpoint (e.g. "http\://host/mcp/sse/")
* `scopes`: OAuth scopes to request. Can be a
* `client_name`: Name for this client during registration
* `token_storage_cache_dir`: Directory for FileTokenStorage
* `additional_client_metadata`: Extra fields for OAuthClientMetadata

**Returns:**

* OAuthClientProvider

## Classes

### `FileTokenStorage` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

File-based token storage implementation for OAuth credentials and tokens.
Implements the mcp.client.auth.TokenStorage protocol.

Each instance is tied to a specific server URL for proper token isolation.

**Methods:**

#### `get_base_url` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_base_url(url: str) -> str
```

Extract the base URL (scheme + host) from a URL.

#### `get_cache_key` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L59" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_cache_key(self) -> str
```

Generate a safe filesystem key from the server's base URL.

#### `get_tokens` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_tokens(self) -> OAuthToken | None
```

Load tokens from file storage.

#### `set_tokens` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L91" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_tokens(self, tokens: OAuthToken) -> None
```

Save tokens to file storage.

#### `get_client_info` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L97" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_client_info(self) -> OAuthClientInformationFull | None
```

Load client information from file storage.

#### `set_client_info` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L125" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_client_info(self, client_info: OAuthClientInformationFull) -> None
```

Save client information to file storage.

#### `clear` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L131" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
clear(self) -> None
```

Clear all cached data for this server.

#### `clear_all` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L140" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
clear_all(cls, cache_dir: Path | None = None) -> None
```

Clear all cached data for all servers.


# client
Source: https://gofastmcp.com/python-sdk/fastmcp-client-client



# `fastmcp.client.client`

## Classes

### `ClientSessionState` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Holds all session-related state for a Client instance.

This allows clean separation of configuration (which is copied) from
session state (which should be fresh for each new client instance).

### `Client` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L90" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

MCP client that delegates connection management to a Transport instance.

The Client class is responsible for MCP protocol logic, while the Transport
handles connection establishment and management. Client provides methods for
working with resources, prompts, tools and other MCP capabilities.

This client supports reentrant context managers (multiple concurrent
`async with client:` blocks) using reference counting and background session
management. This allows efficient session reuse in any scenario with
nested or concurrent client usage.

MCP SDK 1.10 introduced automatic list\_tools() calls during call\_tool()
execution. This created a race condition where events could be reset while
other tasks were waiting on them, causing deadlocks. The issue was exposed
in proxy scenarios but affects any reentrant usage.

The solution uses reference counting to track active context managers,
a background task to manage the session lifecycle, events to coordinate
between tasks, and ensures all session state changes happen within a lock.
Events are only created when needed, never reset outside locks.

This design prevents race conditions where tasks wait on events that get
replaced by other tasks, ensuring reliable coordination in concurrent scenarios.

**Args:**

* `transport`:
  Connection source specification, which can be:

  * ClientTransport: Direct transport instance
  * FastMCP: In-process FastMCP server
  * AnyUrl or str: URL to connect to
  * Path: File path for local socket
  * MCPConfig: MCP server configuration
  * dict: Transport configuration
* `roots`: Optional RootsList or RootsHandler for filesystem access
* `sampling_handler`: Optional handler for sampling requests
* `log_handler`: Optional handler for log messages
* `message_handler`: Optional handler for protocol messages
* `progress_handler`: Optional handler for progress notifications
* `timeout`: Optional timeout for requests (seconds or timedelta)
* `init_timeout`: Optional timeout for initial connection (seconds or timedelta).
  Set to 0 to disable. If None, uses the value in the FastMCP global settings.

**Examples:**

```python
# Connect to FastMCP server
client = Client("http://localhost:8080")

async with client:
    # List available resources
    resources = await client.list_resources()

    # Call a tool
    result = await client.call_tool("my_tool", {"param": "value"})
```

**Methods:**

#### `session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L273" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
session(self) -> ClientSession
```

Get the current active session. Raises RuntimeError if not connected.

#### `initialize_result` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L283" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
initialize_result(self) -> mcp.types.InitializeResult
```

Get the result of the initialization request.

#### `set_roots` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L291" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_roots(self, roots: RootsList | RootsHandler) -> None
```

Set the roots for the client. This does not automatically call `send_roots_list_changed`.

#### `set_sampling_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L295" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_sampling_callback(self, sampling_callback: SamplingHandler) -> None
```

Set the sampling callback for the client.

#### `set_elicitation_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L301" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_elicitation_callback(self, elicitation_callback: ElicitationHandler) -> None
```

Set the elicitation callback for the client.

#### `is_connected` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L309" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
is_connected(self) -> bool
```

Check if the client is currently connected.

#### `new` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L313" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
new(self) -> Client[ClientTransportT]
```

Create a new client instance with the same configuration but fresh session state.

This creates a new client with the same transport, handlers, and configuration,
but with no active session. Useful for creating independent sessions that don't
share state with the original client.

**Returns:**

* A new Client instance with the same configuration but disconnected state.

#### `close` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L476" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
close(self)
```

#### `ping` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L482" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
ping(self) -> bool
```

Send a ping request.

#### `cancel` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L487" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
cancel(self, request_id: str | int, reason: str | None = None) -> None
```

Send a cancellation notification for an in-progress request.

#### `progress` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L504" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
progress(self, progress_token: str | int, progress: float, total: float | None = None, message: str | None = None) -> None
```

Send a progress notification.

#### `set_logging_level` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L516" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_logging_level(self, level: mcp.types.LoggingLevel) -> None
```

Send a logging/setLevel request.

#### `send_roots_list_changed` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L520" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
send_roots_list_changed(self) -> None
```

Send a roots/list\_changed notification.

#### `list_resources_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L526" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resources_mcp(self) -> mcp.types.ListResourcesResult
```

Send a resources/list request and return the complete MCP protocol result.

**Returns:**

* mcp.types.ListResourcesResult: The complete response object from the protocol,
  containing the list of resources and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_resources` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L539" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resources(self) -> list[mcp.types.Resource]
```

Retrieve a list of resources available on the server.

**Returns:**

* list\[mcp.types.Resource]: A list of Resource objects.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_resource_templates_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L551" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resource_templates_mcp(self) -> mcp.types.ListResourceTemplatesResult
```

Send a resources/listResourceTemplates request and return the complete MCP protocol result.

**Returns:**

* mcp.types.ListResourceTemplatesResult: The complete response object from the protocol,
  containing the list of resource templates and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_resource_templates` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L566" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resource_templates(self) -> list[mcp.types.ResourceTemplate]
```

Retrieve a list of resource templates available on the server.

**Returns:**

* list\[mcp.types.ResourceTemplate]: A list of ResourceTemplate objects.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `read_resource_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L580" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
read_resource_mcp(self, uri: AnyUrl | str) -> mcp.types.ReadResourceResult
```

Send a resources/read request and return the complete MCP protocol result.

**Args:**

* `uri`: The URI of the resource to read. Can be a string or an AnyUrl object.

**Returns:**

* mcp.types.ReadResourceResult: The complete response object from the protocol,
  containing the resource contents and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `read_resource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L600" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
read_resource(self, uri: AnyUrl | str) -> list[mcp.types.TextResourceContents | mcp.types.BlobResourceContents]
```

Read the contents of a resource or resolved template.

**Args:**

* `uri`: The URI of the resource to read. Can be a string or an AnyUrl object.

**Returns:**

* list\[mcp.types.TextResourceContents | mcp.types.BlobResourceContents]: A list of content
  objects, typically containing either text or binary data.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_prompts_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L639" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_prompts_mcp(self) -> mcp.types.ListPromptsResult
```

Send a prompts/list request and return the complete MCP protocol result.

**Returns:**

* mcp.types.ListPromptsResult: The complete response object from the protocol,
  containing the list of prompts and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_prompts` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L652" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_prompts(self) -> list[mcp.types.Prompt]
```

Retrieve a list of prompts available on the server.

**Returns:**

* list\[mcp.types.Prompt]: A list of Prompt objects.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `get_prompt_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L665" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_prompt_mcp(self, name: str, arguments: dict[str, Any] | None = None) -> mcp.types.GetPromptResult
```

Send a prompts/get request and return the complete MCP protocol result.

**Args:**

* `name`: The name of the prompt to retrieve.
* `arguments`: Arguments to pass to the prompt. Defaults to None.

**Returns:**

* mcp.types.GetPromptResult: The complete response object from the protocol,
  containing the prompt messages and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `get_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L699" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_prompt(self, name: str, arguments: dict[str, Any] | None = None) -> mcp.types.GetPromptResult
```

Retrieve a rendered prompt message list from the server.

**Args:**

* `name`: The name of the prompt to retrieve.
* `arguments`: Arguments to pass to the prompt. Defaults to None.

**Returns:**

* mcp.types.GetPromptResult: The complete response object from the protocol,
  containing the prompt messages and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `complete_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L720" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
complete_mcp(self, ref: mcp.types.ResourceReference | mcp.types.PromptReference, argument: dict[str, str]) -> mcp.types.CompleteResult
```

Send a completion request and return the complete MCP protocol result.

**Args:**

* `ref`: The reference to complete.
* `argument`: Arguments to pass to the completion request.

**Returns:**

* mcp.types.CompleteResult: The complete response object from the protocol,
  containing the completion and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `complete` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L741" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
complete(self, ref: mcp.types.ResourceReference | mcp.types.PromptReference, argument: dict[str, str]) -> mcp.types.Completion
```

Send a completion request to the server.

**Args:**

* `ref`: The reference to complete.
* `argument`: Arguments to pass to the completion request.

**Returns:**

* mcp.types.Completion: The completion object.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_tools_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L763" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_tools_mcp(self) -> mcp.types.ListToolsResult
```

Send a tools/list request and return the complete MCP protocol result.

**Returns:**

* mcp.types.ListToolsResult: The complete response object from the protocol,
  containing the list of tools and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `list_tools` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L776" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_tools(self) -> list[mcp.types.Tool]
```

Retrieve a list of tools available on the server.

**Returns:**

* list\[mcp.types.Tool]: A list of Tool objects.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `call_tool_mcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L790" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
call_tool_mcp(self, name: str, arguments: dict[str, Any], progress_handler: ProgressHandler | None = None, timeout: datetime.timedelta | float | int | None = None) -> mcp.types.CallToolResult
```

Send a tools/call request and return the complete MCP protocol result.

This method returns the raw CallToolResult object, which includes an isError flag
and other metadata. It does not raise an exception if the tool call results in an error.

**Args:**

* `name`: The name of the tool to call.
* `arguments`: Arguments to pass to the tool.
* `timeout`: The timeout for the tool call. Defaults to None.
* `progress_handler`: The progress handler to use for the tool call. Defaults to None.

**Returns:**

* mcp.types.CallToolResult: The complete response object from the protocol,
  containing the tool result and any additional metadata.

**Raises:**

* `RuntimeError`: If called while the client is not connected.

#### `call_tool` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L826" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
call_tool(self, name: str, arguments: dict[str, Any] | None = None, timeout: datetime.timedelta | float | int | None = None, progress_handler: ProgressHandler | None = None, raise_on_error: bool = True) -> CallToolResult
```

Call a tool on the server.

Unlike call\_tool\_mcp, this method raises a ToolError if the tool call results in an error.

**Args:**

* `name`: The name of the tool to call.
* `arguments`: Arguments to pass to the tool. Defaults to None.
* `timeout`: The timeout for the tool call. Defaults to None.
* `progress_handler`: The progress handler to use for the tool call. Defaults to None.

## **Returns:**

The content returned by the tool. If the tool returns structured
outputs, they are returned as a dataclass (if an output schema
is available) or a dictionary; otherwise, a list of content
blocks is returned. Note: to receive both structured and
unstructured outputs, use call\_tool\_mcp instead and access the
raw result object.

**Raises:**

* `ToolError`: If the tool call results in an error.
* `RuntimeError`: If called while the client is not connected.

### `CallToolResult` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/client.py#L898" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


# elicitation
Source: https://gofastmcp.com/python-sdk/fastmcp-client-elicitation



# `fastmcp.client.elicitation`

## Functions

### `create_elicitation_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/elicitation.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_elicitation_callback(elicitation_handler: ElicitationHandler) -> ElicitationFnT
```

## Classes

### `ElicitResult` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/elicitation.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


# logging
Source: https://gofastmcp.com/python-sdk/fastmcp-client-logging



# `fastmcp.client.logging`

## Functions

### `default_log_handler` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/logging.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
default_log_handler(message: LogMessage) -> None
```

### `create_log_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/logging.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_log_callback(handler: LogHandler | None = None) -> LoggingFnT
```


# messages
Source: https://gofastmcp.com/python-sdk/fastmcp-client-messages



# `fastmcp.client.messages`

## Classes

### `MessageHandler` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

This class is used to handle MCP messages sent to the client. It is used to handle all messages,
requests, notifications, and exceptions. Users can override any of the hooks

**Methods:**

#### `dispatch` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L30" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
dispatch(self, message: Message) -> None
```

#### `on_message` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_message(self, message: Message) -> None
```

#### `on_request` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L77" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_request(self, message: RequestResponder[mcp.types.ServerRequest, mcp.types.ClientResult]) -> None
```

#### `on_ping` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_ping(self, message: mcp.types.PingRequest) -> None
```

#### `on_list_roots` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_list_roots(self, message: mcp.types.ListRootsRequest) -> None
```

#### `on_create_message` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L88" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_create_message(self, message: mcp.types.CreateMessageRequest) -> None
```

#### `on_notification` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L91" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_notification(self, message: mcp.types.ServerNotification) -> None
```

#### `on_exception` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L94" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_exception(self, message: Exception) -> None
```

#### `on_progress` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L97" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_progress(self, message: mcp.types.ProgressNotification) -> None
```

#### `on_logging_message` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_logging_message(self, message: mcp.types.LoggingMessageNotification) -> None
```

#### `on_tool_list_changed` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L105" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_tool_list_changed(self, message: mcp.types.ToolListChangedNotification) -> None
```

#### `on_resource_list_changed` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L110" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_resource_list_changed(self, message: mcp.types.ResourceListChangedNotification) -> None
```

#### `on_prompt_list_changed` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_prompt_list_changed(self, message: mcp.types.PromptListChangedNotification) -> None
```

#### `on_resource_updated` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L120" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_resource_updated(self, message: mcp.types.ResourceUpdatedNotification) -> None
```

#### `on_cancelled` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/messages.py#L125" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
on_cancelled(self, message: mcp.types.CancelledNotification) -> None
```


# oauth_callback
Source: https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback



# `fastmcp.client.oauth_callback`

OAuth callback server for handling authorization code flows.

This module provides a reusable callback server that can handle OAuth redirects
and display styled responses to users.

## Functions

### `create_callback_html` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/oauth_callback.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_callback_html(message: str, is_success: bool = True, title: str = 'FastMCP OAuth', server_url: str | None = None) -> str
```

Create a styled HTML response for OAuth callbacks.

### `create_oauth_callback_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/oauth_callback.py#L197" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_oauth_callback_server(port: int, callback_path: str = '/callback', server_url: str | None = None, response_future: asyncio.Future | None = None) -> Server
```

Create an OAuth callback server.

**Args:**

* `port`: The port to run the server on
* `callback_path`: The path to listen for OAuth redirects on
* `server_url`: Optional server URL to display in success messages
* `response_future`: Optional future to resolve when OAuth callback is received

**Returns:**

* Configured uvicorn Server instance (not yet running)

## Classes

### `CallbackResponse` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/oauth_callback.py#L183" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `from_dict` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/oauth_callback.py#L190" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_dict(cls, data: dict[str, str]) -> CallbackResponse
```

#### `to_dict` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/oauth_callback.py#L193" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_dict(self) -> dict[str, str]
```


# progress
Source: https://gofastmcp.com/python-sdk/fastmcp-client-progress



# `fastmcp.client.progress`

## Functions

### `default_progress_handler` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/progress.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
default_progress_handler(progress: float, total: float | None, message: str | None) -> None
```

Default handler for progress notifications.

Logs progress updates at debug level, properly handling missing total or message values.

**Args:**

* `progress`: Current progress value
* `total`: Optional total expected value
* `message`: Optional status message


# roots
Source: https://gofastmcp.com/python-sdk/fastmcp-client-roots



# `fastmcp.client.roots`

## Functions

### `convert_roots_list` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/roots.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
convert_roots_list(roots: RootsList) -> list[mcp.types.Root]
```

### `create_roots_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/roots.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_roots_callback(handler: RootsList | RootsHandler) -> ListRootsFnT
```


# sampling
Source: https://gofastmcp.com/python-sdk/fastmcp-client-sampling



# `fastmcp.client.sampling`

## Functions

### `create_sampling_callback` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/sampling.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
create_sampling_callback(sampling_handler: SamplingHandler) -> SamplingFnT
```


# transports
Source: https://gofastmcp.com/python-sdk/fastmcp-client-transports



# `fastmcp.client.transports`

## Functions

### `infer_transport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L847" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
infer_transport(transport: ClientTransport | FastMCP | FastMCP1Server | AnyUrl | Path | MCPConfig | dict[str, Any] | str) -> ClientTransport
```

Infer the appropriate transport type from the given transport argument.

This function attempts to infer the correct transport type from the provided
argument, handling various input types and converting them to the appropriate
ClientTransport subclass.

The function supports these input types:

* ClientTransport: Used directly without modification
* FastMCP or FastMCP1Server: Creates an in-memory FastMCPTransport
* Path or str (file path): Creates PythonStdioTransport (.py) or NodeStdioTransport (.js)
* AnyUrl or str (URL): Creates StreamableHttpTransport (default) or SSETransport (for /sse endpoints)
* MCPConfig or dict: Creates MCPConfigTransport, potentially connecting to multiple servers

For HTTP URLs, they are assumed to be Streamable HTTP URLs unless they end in `/sse`.

For MCPConfig with multiple servers, a composite client is created where each server
is mounted with its name as prefix. This allows accessing tools and resources from multiple
servers through a single unified client interface, using naming patterns like
`servername_toolname` for tools and `protocol://servername/path` for resources.
If the MCPConfig contains only one server, a direct connection is established without prefixing.

**Examples:**

```python
# Connect to a local Python script
transport = infer_transport("my_script.py")

# Connect to a remote server via HTTP
transport = infer_transport("http://example.com/mcp")

# Connect to multiple servers using MCPConfig
config = {
    "mcpServers": {
        "weather": {"url": "http://weather.example.com/mcp"},
        "calendar": {"url": "http://calendar.example.com/mcp"}
    }
}
transport = infer_transport(config)
```

## Classes

### `SessionKwargs` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Keyword arguments for the MCP ClientSession constructor.

### `ClientTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Abstract base class for different MCP client transport mechanisms.

A Transport is responsible for establishing and managing connections
to an MCP server, and providing a ClientSession within an async context.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

Establishes a connection and yields an active ClientSession.

The ClientSession is *not* expected to be initialized in this context manager.

The session is guaranteed to be valid only within the scope of the
async context manager. Connection setup and teardown are handled
within this context.

**Args:**

* `**session_kwargs`: Keyword arguments to pass to the ClientSession
  constructor (e.g., callbacks, timeouts).

#### `close` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L106" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
close(self)
```

Close the transport.

### `WSTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport implementation that connects to an MCP server via WebSockets.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L133" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

### `SSETransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L154" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport implementation that connects to an MCP server via Server-Sent Events.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L190" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

### `StreamableHttpTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L226" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport implementation that connects to an MCP server via Streamable HTTP Requests.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L262" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

### `StdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L299" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Base transport for connecting to an MCP server via subprocess with stdio.

This is a base class that can be subclassed for specific command-based
transports like Python, Node, Uvx, etc.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L342" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

#### `connect` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L355" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect(self, **session_kwargs: Unpack[SessionKwargs]) -> ClientSession | None
```

#### `disconnect` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L406" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
disconnect(self)
```

#### `close` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L421" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
close(self)
```

### `PythonStdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L430" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for running Python scripts.

### `FastMCPStdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L476" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for running FastMCP servers using the FastMCP CLI.

### `NodeStdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L503" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for running Node.js scripts.

### `UvxStdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L545" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for running commands via the uvx tool.

### `NpxStdioTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L611" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for running commands via the npx tool.

### `FastMCPTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L673" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

In-memory transport for FastMCP servers.

This transport connects directly to a FastMCP server instance in the same
Python process. It works with both FastMCP 2.x servers and FastMCP 1.0
servers from the low-level MCP SDK. This is particularly useful for unit
tests or scenarios where client and server run in the same runtime.

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L692" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```

### `MCPConfigTransport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L727" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Transport for connecting to one or more MCP servers defined in an MCPConfig.

This transport provides a unified interface to multiple MCP servers defined in an MCPConfig
object or dictionary matching the MCPConfig schema. It supports two key scenarios:

1. If the MCPConfig contains exactly one server, it creates a direct transport to that server.
2. If the MCPConfig contains multiple servers, it creates a composite client by mounting
   all servers on a single FastMCP instance, with each server's name, by default, used as its mounting prefix.

In the multi-server case, tools are accessible with the prefix pattern `{server_name}_{tool_name}`
and resources with the pattern `protocol://{server_name}/path/to/resource`.

This is particularly useful for creating clients that need to interact with multiple specialized
MCP servers through a single interface, simplifying client code.

**Examples:**

```python
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig

# Create a config with multiple servers
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather-api.example.com/mcp",
            "transport": "http"
        },
        "calendar": {
            "url": "https://calendar-api.example.com/mcp",
            "transport": "http"
        }
    }
}

# Create a client with the config
client = Client(config)

async with client:
    # Access tools with prefixes
    weather = await client.call_tool("weather_get_forecast", {"city": "London"})
    events = await client.call_tool("calendar_list_events", {"date": "2023-06-01"})

    # Access resources with prefixed URIs
    icons = await client.read_resource("weather://weather/icons/sunny")
```

**Methods:**

#### `connect_session` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/transports.py#L799" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
connect_session(self, **session_kwargs: Unpack[SessionKwargs]) -> AsyncIterator[ClientSession]
```


# exceptions
Source: https://gofastmcp.com/python-sdk/fastmcp-exceptions



# `fastmcp.exceptions`

Custom exceptions for FastMCP.

## Classes

### `FastMCPError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L6" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Base error for FastMCP.

### `ValidationError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L10" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Error in validating parameters or return values.

### `ResourceError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Error in resource operations.

### `ToolError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Error in tool operations.

### `PromptError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Error in prompt operations.

### `InvalidSignature` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Invalid signature for use with FastMCP.

### `ClientError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L30" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Error in client operations.

### `NotFoundError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Object not found.

### `DisabledError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/exceptions.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Object is disabled.


# mcp_config
Source: https://gofastmcp.com/python-sdk/fastmcp-mcp_config



# `fastmcp.mcp_config`

Canonical MCP Configuration Format.

This module defines the standard configuration format for Model Context Protocol (MCP) servers.
It provides a client-agnostic, extensible format that can be used across all MCP implementations.

The configuration format supports both stdio and remote (HTTP/SSE) transports, with comprehensive
field definitions for server metadata, authentication, and execution parameters.

Example configuration:

```json
{
    "mcpServers": {
        "my-server": {
            "command": "npx",
            "args": ["-y", "@my/mcp-server"],
            "env": {"API_KEY": "secret"},
            "timeout": 30000,
            "description": "My MCP server"
        }
    }
}
```

## Functions

### `infer_transport_type_from_url` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
infer_transport_type_from_url(url: str | AnyUrl) -> Literal['http', 'sse']
```

Infer the appropriate transport type from the given URL.

### `update_config_file` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L293" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
update_config_file(file_path: Path, server_name: str, server_config: CanonicalMCPServerTypes) -> None
```

Update an MCP configuration file from a server object, preserving existing fields.

This is used for updating the mcpServer configurations of third-party tools so we do not
worry about transforming server objects here.

## Classes

### `StdioMCPServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L110" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

MCP server configuration for stdio transport.

This is the canonical configuration format for MCP servers using stdio transport.

**Methods:**

#### `to_transport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L140" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_transport(self) -> StdioTransport
```

### `TransformingStdioMCPServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L151" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A Stdio server with tool transforms.

### `RemoteMCPServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L155" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

MCP server configuration for HTTP/SSE transport.

This is the canonical configuration format for MCP servers using remote transports.

**Methods:**

#### `to_transport` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L191" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_transport(self) -> StreamableHttpTransport | SSETransport
```

### `TransformingRemoteMCPServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L216" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A Remote server with tool transforms.

### `MCPConfig` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L227" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A configuration object for MCP Servers that conforms to the canonical MCP configuration format
while adding additional fields for enabling FastMCP-specific features like tool transformations
and filtering by tags.

For an MCPConfig that is strictly canonical, see the `CanonicalMCPConfig` class.

**Methods:**

#### `validate_mcp_servers` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L240" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
validate_mcp_servers(self, info: ValidationInfo) -> dict[str, Any]
```

Validate the MCP servers.

#### `add_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L250" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
add_server(self, name: str, server: MCPServerTypes) -> None
```

Add or update a server in the configuration.

#### `from_dict` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L255" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_dict(cls, config: dict[str, Any]) -> Self
```

Parse MCP configuration from dictionary format.

#### `to_dict` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L259" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_dict(self) -> dict[str, Any]
```

Convert MCPConfig to dictionary format, preserving all fields.

#### `write_to_file` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L263" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
write_to_file(self, file_path: Path) -> None
```

Write configuration to JSON file.

#### `from_file` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L269" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_file(cls, file_path: Path) -> Self
```

Load configuration from JSON file.

### `CanonicalMCPConfig` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L278" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Canonical MCP configuration format.

This defines the standard configuration format for Model Context Protocol servers.
The format is designed to be client-agnostic and extensible for future use cases.

**Methods:**

#### `add_server` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/mcp_config.py#L288" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
add_server(self, name: str, server: CanonicalMCPServerTypes) -> None
```

Add or update a server in the configuration.


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-prompts-__init__



# `fastmcp.prompts`

*This module is empty or contains only private/internal implementations.*


# prompt
Source: https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt



# `fastmcp.prompts.prompt`

Base classes for FastMCP prompts.

## Functions

### `Message` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L31" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
Message(content: str | ContentBlock, role: Role | None = None, **kwargs: Any) -> PromptMessage
```

A user-friendly constructor for PromptMessage.

## Classes

### `PromptArgument` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L53" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

An argument that can be passed to a prompt.

### `Prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L65" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A prompt template that can be rendered with parameters.

**Methods:**

#### `enable` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L72" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
enable(self) -> None
```

#### `disable` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
disable(self) -> None
```

#### `to_mcp_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L88" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_mcp_prompt(self, **overrides: Any) -> MCPPrompt
```

Convert the prompt to an MCP prompt.

#### `from_function` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_function(fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, title: str | None = None, description: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionPrompt
```

Create a Prompt from a function.

The function can return:

* A string (converted to a message)
* A Message object
* A dict (converted to a message)
* A sequence of any of the above

#### `render` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L133" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
render(self, arguments: dict[str, Any] | None = None) -> list[PromptMessage]
```

Render the prompt with arguments.

### `FunctionPrompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L141" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A prompt that is a function.

**Methods:**

#### `from_function` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L147" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_function(cls, fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, title: str | None = None, description: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionPrompt
```

Create a Prompt from a function.

The function can return:

* A string (converted to a message)
* A Message object
* A dict (converted to a message)
* A sequence of any of the above

#### `render` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt.py#L305" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
render(self, arguments: dict[str, Any] | None = None) -> list[PromptMessage]
```

Render the prompt with arguments.


# prompt_manager
Source: https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager



# `fastmcp.prompts.prompt_manager`

## Classes

### `PromptManager` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Manages FastMCP prompts.

**Methods:**

#### `mount` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L45" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
mount(self, server: MountedServer) -> None
```

Adds a mounted server as a source for prompts.

#### `has_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
has_prompt(self, key: str) -> bool
```

Check if a prompt exists.

#### `get_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L94" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_prompt(self, key: str) -> Prompt
```

Get prompt by key.

#### `get_prompts` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L101" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_prompts(self) -> dict[str, Prompt]
```

Gets the complete, unfiltered inventory of all prompts.

#### `list_prompts` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_prompts(self) -> list[Prompt]
```

Lists all prompts, applying protocol filtering.

#### `add_prompt_from_fn` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
add_prompt_from_fn(self, fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, description: str | None = None, tags: set[str] | None = None) -> FunctionPrompt
```

Create a prompt from a function.

#### `add_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
add_prompt(self, prompt: Prompt) -> Prompt
```

Add a prompt to the manager.

#### `render_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/prompts/prompt_manager.py#L152" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
render_prompt(self, name: str, arguments: dict[str, Any] | None = None) -> GetPromptResult
```

Internal API for servers: Finds and renders a prompt, respecting the
filtered protocol path.


# __init__
Source: https://gofastmcp.com/python-sdk/fastmcp-resources-__init__



# `fastmcp.resources`

*This module is empty or contains only private/internal implementations.*


# resource
Source: https://gofastmcp.com/python-sdk/fastmcp-resources-resource



# `fastmcp.resources.resource`

Base classes and interfaces for FastMCP resources.

## Classes

### `Resource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Base class for all resources.

**Methods:**

#### `enable` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
enable(self) -> None
```

#### `disable` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
disable(self) -> None
```

#### `from_function` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_function(fn: Callable[..., Any], uri: str | AnyUrl, name: str | None = None, title: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResource
```

#### `set_default_mime_type` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L87" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_default_mime_type(cls, mime_type: str | None) -> str
```

Set default MIME type if not provided.

#### `set_default_name` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L94" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_default_name(self) -> Self
```

Set default name from URI if not provided.

#### `read` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L105" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
read(self) -> str | bytes
```

Read the resource content.

#### `to_mcp_resource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L109" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
to_mcp_resource(self, **overrides: Any) -> MCPResource
```

Convert the resource to an MCPResource.

#### `key` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
key(self) -> str
```

The key of the component. This is used for internal bookkeeping
and may reflect e.g. prefixes or other identifiers. You should not depend on
keys having a certain value, as the same tool loaded from different
hierarchies of servers may have different keys.

### `FunctionResource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A resource that defers data loading by wrapping a function.

The function is only called when the resource is read, allowing for lazy loading
of potentially expensive data. This is particularly useful when listing resources,
as the function won't be called until the resource is actually accessed.

The function can return:

* str for text content (default)
* bytes for binary content
* other types will be converted to JSON

**Methods:**

#### `from_function` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L150" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_function(cls, fn: Callable[..., Any], uri: str | AnyUrl, name: str | None = None, title: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResource
```

Create a FunctionResource from a function.

#### `read` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource.py#L175" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
read(self) -> str | bytes
```

Read the resource by calling the wrapped function.


# resource_manager
Source: https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager



# `fastmcp.resources.resource_manager`

Resource manager functionality.

## Classes

### `ResourceManager` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Manages FastMCP resources.

**Methods:**

#### `mount` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
mount(self, server: MountedServer) -> None
```

Adds a mounted server as a source for resources and templates.

#### `get_resources` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_resources(self) -> dict[str, Resource]
```

Get all registered resources, keyed by URI.

#### `get_resource_templates` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_resource_templates(self) -> dict[str, ResourceTemplate]
```

Get all registered templates, keyed by URI template.

#### `list_resources` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resources(self) -> list[Resource]
```

Lists all resources, applying protocol filtering.

#### `list_resource_templates` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L175" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
list_resource_templates(self) -> list[ResourceTemplate]
```

Lists all templates, applying protocol filtering.

#### `add_resource_or_template_from_fn` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/resources/resource_manager.py#L182


'''

# 测试提示词列表
test_prompts = [
    "FastMCP 1.x 和 2.x 在「服务器组合、代理以及 OpenAPI → MCP 生成」这三点上到底新增了哪些 API？有无迁移指南或破坏性变更列表",
    "STDIO 与 SSE 两种传输方式在「进程生命周期、并发模型、连接复用」上的底层差异是什么？文档里是否给出了选择建议或性能基准?",
    "当「初始化参数、环境变量、dotenv 文件、运行时 run() 参数」同时出现时，真正的优先级顺序和合并规则是什么？",
    "on_duplicate_tools / resources / prompts 三个配置项在冲突时到底会抛出异常、忽略还是后覆盖前？有无调试日志可追踪？",
    "Pydantic 支持的所有类型（含自定义类型）都能被 FastMCP 正确序列化/反序列化吗？对于无法隐式转换的值，异常格式是什么样的？",
    "ctx.get_http_request() 仅在 SSE 或 streamable-http 模式下可用，还是 STDIO 也能用？文档是否列出了所有可用的上下文属性及线程安全保证？",
    "官方 Client 在 async with 块外是否保持 TCP 连接？高频调用时是否需要手动连接池？文档有无给出最佳实践？",
    "FastMCP 如何将 OpenAPI 的 path / query / header / body 参数一一映射到 MCP tool 的 schema？对于 anyOf / oneOf / allOf 这类复杂 schema 有无示例？",
    "官方文档是否给出了「认证、鉴权、HTTPS、CORS、日志脱敏」等安全加固的完整示例或推荐插件？",
    "除了 log_level 外，FastMCP 是否内置 tracing/metrics 钩子？文档里是否提供了与 Prometheus、OpenTelemetry 集成的例子",
    ]