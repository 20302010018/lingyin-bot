from revChatGPT.revChatGPT import Chatbot

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
chatgpt_session_token_list = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..yJWa-fql3_h9s4lk.aWMthmJUMSlGMv5FADfMYcjhTXxgYUevjm1aBDUzxFKhPeZOgpoCHDw8He5gznw6MmKANQIykr5uGse5bZgcYhcOgRYiTRHQHbJNdhpIKQqKmKdi0IjxlTk_3SK8MLp59NnnhthU5NRL7lwWExbq9c0l9t89qB7dKU0PfbEUmywpyRTB9ZVl3mDrktWP4pCISG2Td1s1or78fHfF2x7e7Zo4_HAJbxBBEwzCL2z7xY6qNRDzikIHArTxhxt1XuoYGmsjHn2Lxy1Ei1LUbkTtLBno4ifQumQJ1EgnQwf80SGtKF0G_fIMBHeppFTg_BFSyVUAw5Wmj40Q81npeyKWQuRsDWkC7o6cNum3AKFWtBlHp9zSpk086xbjseEtIoMiWU2gmUJStE9iqFdzh138WzXXKkjRfv5M89zjd3XC2z1zfoOVT07OCrxziJpBJzGxtiuG7mZD63GjHDOfE5bcK8yvdZg8tiBPsrqxqF20TOCjQvqOMqVEpLUCSf35_ywgQeUt-3H6QU2KqX1yhhYSjOUy6-nTeljAQsWv9BYNuDGoMF6abcpDBa-mqiXAqTj9lOYrBQSG42DAEYHETeyfsxnnlxR-k_oCElUEWiGpt1HTXnsCUkoxMS-uWcArjCocEotFyr-BCUZRhUgfypEwu34OllGQdIgMEtCtLxD-fiDwS54F8Bk_UUiuzCCRkiM9OcSzK_6taWZ3x9wMgYWvYdmEVYWre8vyoLWszU9WSK30bER-yCXpBaUtQoab6LmvG2uU73YeQXohcp_V9vdDAVv7gbYI1pcX0t8s8VKG9M_lEeP5-lm9WB7UZWxfX9wvVyINmsqf_OjsnHh9VwXXqrWthHQJ9nrSfbbnefm-RVJnYw0KoCKbLY7HaWNpsqGXIBCUvpUD3-EXeu1u3DFAgjdRBNUYTod6Dl0ON5Tlrnu-h4CXrz8fBtH3VlOz5_hxspmGwLonoiAzIMml0ibfNOur2we7MRskub_j7CQZ75U8zWgcSnx8nQ7vj_D9MLpbUdJgaJUgN0xu0nYg5QeTnnUZpDX6v6Y8Yw_RZaFAt5_ZcVzukx90kFNXwPXlFVE2VTyZyfqNwkAaV2EbvRVnKeHw2nWXqDsvKt-3sqTxtnlv2sJJPYqlIAVv-Sri82_Y-WMCom-LZC0_G0vNPXLqYSOQkLOhCqF6niR_LO2xStTmm60H9rfkAzipcNHK6wHr5B-btG7aQY4BUqXB7gq9ZB7BWNVXffBiO5Yd6-SGRzWFixM9OP2yXt--nsO4dacj092K1WovD3gGfo9Adwuo_XMZAZlqt6i41THzCsT-cHIe9RhuyDsgt8VuxUWyO-SR8elK7wx-soDiTe0Fr077sGTbqj3tT8T7hxH79hqM0Rynot-ksqQETLV56e9LTxZ8JLNHBLvqz1x7Z5axyyoMzw_Hyxtz2hk-ard85Vcopa1Zn251S5geIzoQpxRV4_UdvQRvcmNuQpmZTnhrkZxTwneI1oxzqFUtc-J9hjWvMy7zV89dg_1_8qO2XSefNqJ40tym9yzAjr7D6_QSUqbGOW7kRB3xWJ7YTeqFvG9BVFnA1eNtkGBpNrWr_VOjQbScov0ggQ5AH4TUUILLyXgfMkAGliqQH23S0lPBX2LwYQX4LwFahU7F3NL8HVqjL5BJZp2x-DryBPDRcIcS5EVBA7bQVyOGAC3NUg0tZ4DD-MPbq6E8lscnMmNlBf7FPWmZQFoclz24lDVmsMwaOHoYVLVT4556h-8bZWOkbF8LpGUkUenvZkQZJCiNAVADA6BlfqP5R2t_rsZTskcVBbTkkPX2Xl2Stk31lFYMNOTqMqtQpdvNDEV5UFAiGLOHEbBF0G3TsTMeUUEztmp-e0KdN1XY8291IxVpksesHpT3k2YgyTYc7Yw-c5v2BF3C-yPv1PQIxTssEm2vUrZNOhKm-DQZM-KylxYVAO9vImQE4-MSb6eEqCwp5-5yquinOE9kMkJoaj6ZL7l1bDYtsnjxBcyAbTxVkjUCH4wLZo_OKEPIGhf_9F8BEvw7lTA7pcwrPFyHoM86CT4N6UU8Qtd2-erNGv_h8zE2_t3Vteb2vlgcrMpiOPG3Ycjf7yf0uUrjPAO2b07HvaQqNKA5ntFVIT_6bZaku6ysCIOGDW3MjPnNvZ0Eo6937ng3Jqt4ohWd7mzmrLHQtQoiV3gOn4irrYqBDSfVu2NsHH-dNCCgUSl1JJ5O4t1zEIUyYzmIG5c7szpS2KJKA7RE4g.5ymJ_8gPrN064vfSTR7EBw"
chatgpt_cf_clearance = "UfRzPvxFA1z4HTHTq5BSdYh9WD_Dix6Cq8c9LmYqPFo-1670820165-0-160"

config = {
  "session_token": chatgpt_session_token_list,
  "cf_clearance": chatgpt_cf_clearance,
  "user_agent": agent
}


chatbot = Chatbot(config, conversation_id=None, debug=True)
res = chatbot.get_chat_response("hello")

print(res)