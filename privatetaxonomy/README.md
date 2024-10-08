Adding a private taxonomy
```
$ cd /var/www/MISP/app/files/taxonomies/
$ mkdir privatetaxonomy
$ cd privatetaxonomy
$ vi machinetag.json
```

Create a JSON file describing your taxonomy as triple tags.

For example :
```
mkdir sample
cd sample
vim machinetag.json
```


Sample JSON with triple tags. You can use the JSON validator to be sure that there is no syntax error.
```json
{
  "namespace": "sample",
  "description": "Some descriptive words",
  "version": 1,
  "predicates": [
    {
      "value": "my-predicate",
      "expanded": "my-predicate"
    }
  ],
  "values": [
    {
      "predicate": "my-predicate",
      "entry": [
        {
          "value": "a-value",
          "expanded": "A value"
        }
      ]
    }
  ]
}
```
Go to MISP Web GUI taxonomies/index and update the taxonomies once you are happy with your file. The newly created taxonomy should be visible. Now you need to activate the tags within your taxonomy.


An example extracted from `/var/www/MISP/app/files/taxonomies/ransomware/machinetag.json`:

```json
{
  "namespace": "ransomware",
  "expanded": "ransomware types and elements",
  "description": "Ransomware is used to define ransomware types and the elements that compose them.",
  "version": 6,
  "refs": [
    "https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-evolution-of-ransomware.pdf",
    "https://docs.apwg.org/ecrimeresearch/2018/5357083.pdf",
    "https://bartblaze.blogspot.com/p/the-purpose-of-ransomware.html",
    "https://arxiv.org/pdf/2102.06249.pdf"
  ],
  "predicates": [
    {
      "value": "type",
      "expanded": "Type",
      "description": "Type is used to describe the type of a ransomware and how it works."
    },
    {
      "value": "element",
      "expanded": "Element",
      "description": "Elements that composed or are linked to a ransomware and its execution."
    },
    {
      "value": "complexity-level",
      "expanded": "Complexity level",
      "description": "Level of complexity of the ransomware."
    },
    {
      "value": "purpose",
      "expanded": "Purpose",
      "description": "Purpose of the ransomware."
    },
    {
      "value": "target",
      "expanded": "Target",
      "description": "Target of the ransomware."
    },
    {
      "value": "infection",
      "expanded": "Infection",
      "description": "Infection vector used by the ransomware."
    },
    {
      "value": "communication",
      "expanded": "Communication",
      "description": "Communication method used by the ransomware;"
    },
    {
      "value": "malicious-action",
      "expanded": "Malicious Action",
      "description": "Malicious action performed by the ransomware."
    }
  ],
  "values": [
    {
      "predicate": "type",
      "entry": [
        {
          "value": "scareware",
          "expanded": "Scareware is a form of malware which uses social engineering to cause shock, anxiety, or the perception of a threat in order to manipulate users into buying unwanted software."
        },
        {
          "value": "locker-ransomware",
          "expanded": "Locker ransomware, also called screen locker, denies access to the browser, computer or device."
        },
        {
          "value": "crypto-ransomware",
          "expanded": "Crypto ransomware, also called data locker or cryptoware, prevents access to files or data. Crypto ransomware doesn’t necessarily have to use encryption to stop users from accessing their data, but the vast majority of it does."
        }
      ]
    },
    {
      "predicate": "element",
      "entry": [
        {
          "value": "ransomnote",
          "expanded": "A ransomnote is the message left by the attacker to threaten their victim and ask for a ransom. It is usually seen as a text or HTML file, or a picture set as background."
        },
        {
          "value": "ransomware-appended-extension",
          "expanded": "This is the extension added by the ransomware to the files."
        },
        {
          "value": "ransomware-encrypted-extensions",
          "expanded": "This is the list of extensions that will be encrypted by the ransomware. Beware to keep the order."
        },
        {
          "value": "ransomware-excluded-extensions",
          "expanded": "This is the list of extensions that will not be encrypted by the ransomware. Beware to keep the order."
        },
        {
          "value": "dropper",
          "expanded": "A dropper is a means of getting malware into a machine while bypassing the security checks, often by containing the malware inside of itself."
        },
        {
          "value": "downloader",
          "expanded": "A downloader is a means of getting malware into a machine while bypassing the security checks, by downloading it instead of containing it."
        }
      ]
    },
    {
      "predicate": "complexity-level",
      "entry": [
        {
          "value": "no-actual-encryption-scareware",
          "expanded": "No actual encryption (scareware). Infection merely poses as a ransomware by displaying a ransom note or message while not actually encrypting user files."
        },
        {
          "value": "display-ransomnote-before-encrypting",
          "expanded": "Displaying the ransom note before the encryption process commences. As seen in the case of Nemucod, some ransomware will display a ransom note before file encryption. This is a serious operational flaw in the ransomware. The victim or their antivirus solution could effectively take prompt evasive action to prevent ransomware from commencing encryption."
        },
        {
          "value": "decryption-essentials-extracted-from-binary",
          "expanded": "Decryption essentials can be reverse engineered from ransomware code or the user's system. For example, if the ransomware uses a hard-coded key, then it becomes straight-forward for malware analysts to extract the key by reverse engineering the ransomware binary. "
        },
        {
          "value": "derived-encryption-key-predicted  ",
          "expanded": "Another possibility of reverse engineering the key is demonstrated in the case of Linux.Encoder, a type of ransomware where a timestamp on the system was used to create keys for encryption resulting in easy decryption provided that the timestamp is still accessible."
        },
        {
          "value": "same-key used-for-each-infection",
          "expanded": "Ransomware uses the same key for every victim. If the same key is used to encrypt all victims during a campaign, then one victim can share the secret key with others."
        },
        {
          "value": "encryption-circumvented",
          "expanded": "Decryption possible without key - files can be decrypted without the need for a key due to poor choice or implementation of the encryption algorithm. Consider the case of desuCrypt that used an RC4 stream cipher for encryption. Using a stream cipher with key reuse is vulnerable to known plaintext attacks and known ciphertext attacks due to key reuse and hence this is a poor implementation of an encryption algorithm."
        },
        {
          "value": "file-restoration-possible-using-shadow-volume-copies",
          "expanded": "Files can be restored using Shadow Volume Copies (“Previous Versions”) on the New Technology File System (NTFS), that were neglected to be deleted by the ransomware."
        },
        {
          "value": "file-restoration-possible-using-backups",
          "expanded": "Files can be restored using a System State backup, System Image backup or other means of backup mechanisms (such as third-party backup software) that will render the ransomware's extortion attempt unsuccessful."
        },
        {
          "value": "key-recovered-from-file-system-or-memory",
          "expanded": "Decryption key can be retrieved from the host machine’s file structure or memory by an average user without the need for an expert. In the case of CryptoDefense, the ransomware did not securely delete keys from the host machine. The user can examine the right file or folder to discover the decryption key."
        },
        {
          "value": "due-diligence-prevented-ransomware-from-acquiring-key",
          "expanded": "User can prevent ransomware from acquiring the encryption key. Ransomware belongs in this category if its encryption procedure can be interrupted or blocked by due diligence on part of the user. For example, CryptoLocker discussed above cannot commence operation until it receives a key from the C&C server. A host or border firewall can block a list of known C&C servers hence rendering ransomware ineffective."
        },
        {
          "value": "click-and-run-decryptor-exists",
          "expanded": "Easy “Click-and-run” solutions such as a decryptor has been created by the security community such that a user can simply run the program to decrypt all files."
        },
        {
          "value": "kill-switch-exists-outside-of-attacker-s-control",
          "expanded": "There exists a kill switch outside of an attacker’s control that renders the cryptoviral infection ineffective. For example, in the case of WannaCry, a global kill switch existed in the form of a domain name. The ransomware reached out to this domain before commencing encryption and if the domain existed, the ransomware aborted execution. This kill switch was outside the attacker’s control as anyone could register it and neutralize the ransomware outbreak."
        },
        {
          "value": "decryption-key-recovered-from-a-C&C-server-or-network-communications",
          "expanded": "Key can be retrieved from a central location such as a C&C server on a compromised host or gleaned with some difficulty from communication between ransomware on the host and the C&C server. For instance, in the case of CryptoLocker, authorities were able to seize a network of compromised hosts used to spread CryptoLocker and gain access to decryption essentials of around 500,000 victims."
        },
        {
          "value": "custom-encryption-algorithm-used",
          "expanded": "Ransomware uses custom encryption techniques and violates the fundamental rule of cryptography: “do not roll your own crypto.” It is tempting to design a custom cipher that one cannot break themselves, however it will likely not withstand the scrutiny of professional cryptanalysts. Amateur custom cryptography in the ransomware implies there will likely soon be a solution to decrypt files without paying the ransom. An example of this is an early variant of the GPCode ransomware that emerged in 2005 with weak custom encryption."
        },
        {
          "value": "decryption-key-recovered-under-specialized-lab-setting",
          "expanded": "Key can only be retrieved under rare, specialized laboratory settings. For example, in the case of WannaCry, a vulnerability in a cryptographic API on an unpatched Windows XP system allowed users to acquire from RAM the prime numbers used to compute private keys and hence retrieve the decryption key. However, the victim had to have been running a specific version of Windows XP and be fortunate enough that the related address space in memory has not been reallocated to another process. In another example, it is theoretically possible to reverse WannaCry encryption by exploiting a flaw in the pseudo-random-number-generator (PRNG) in an unpatched Windows XP system that reveals keys generated in the past. Naturally, these specialized conditions are not true for most victims."
        },
        {
          "value": "small-subset-of-files-left-unencrypted",
          "expanded": "A small subset of files left unencrypted by the ransomware for any number of reasons. Certain ransomware are known to only encrypt a file if its size exceeds a predetermined value. In addition, ransomware might decrypt a few files for free to prove decryption is possible. In such cases, a small number of victims may be lucky enough to only need these unencrypted files and can tolerate loss of the rest."
        },
        {
          "value": "encryption-model-is-seemingly-flawless",
          "expanded": "Encryption model is resistant to cryptographic attacks and has been implemented seemingly flawlessly such that there are no known vulnerabilities in its execution. Simply put, there is no proven way yet to decrypt the files without paying the ransom."
        }
      ]
    },
    {
      "predicate": "purpose",
      "entry": [
        {
          "value": "deployed-as-ransomware-extortion",
          "expanded": "This has been the traditional approach - ransomware is installed on the victim's machine, and its only purpose is to create income for the cybercriminal(s).  In fact, ransomware is simple extortion, but via digital means."
        },
        {
          "value": "deployed-to-showcase-skills-for-fun-or-for-testing-purposes",
          "expanded": "Some cybercriminals like to show off, and as such create the side-business of ransomware, or, more particularly to showcase their coding skills.\nAnother example may be to send ransomware 'as a joke' or for fun to your friends, and giving them a bad time.\nSome cybercriminals may be testing the waters by deploying ransomware in an organisation, to stress-test the defenses, or to test their own programming skills, or the lack thereof."
        },
        {
          "value": "deployed-as-smokescreen",
          "expanded": "A very interesting occurrence indeed: ransomware is installed to hide the real purpose of whatever the cybercriminal or attacker is doing. This may be data exfiltration, lateral movement, or anything else, in theory, everything is a possible scenario... except for the ransomware itself."
        },
        {
          "value": "deployed-to-cause-frustration",
          "expanded": "Another possible angle that goes hand in hand with the classic extortion scheme - deploying ransomware with intent of frustrating the victim. Basically, cyber bullying. While there may be a request for a monetary amount, it is not the purpose."
        },
        {
          "value": "deployed-out-of-frustration",
          "expanded": "Sometimes, an attacker may gain initial access to a server or other machine, but consequent attempts to, for example, exfiltrate data or attack other machine, is unsuccessful. This may be due to a number of things, but often due to the access being discovered, and quickly patched. On the other hand, it may have not been discovered yet, but the attacker is sitting with the same problem: the purpose is not fulfilled. Then, out of frustration, or to gain at least something out of the victim, the machine gets trashed with ransomware. Another possibility is a disgruntled employee, leaving ransomware as a 'present' before leaving the company."
        },
        {
          "value": "deployed-as-a-cover-up",
          "expanded": "This may sound ambiguous at first, but imagine a scenario where a company may face sanctions, is already compromised, or has a running investigation. The company or organisation deploying ransomware itself, is a viable way of destroying data forever, and any evidence may be lost.\nAnother possibility is, in order to cover up a much larger compromise, ransomware is installed, and everything is formatted to hide what actually happened.\nAgain, there is also the possibility of a disgruntled employee, or even an intruder: which brings us back to 'deployed as a smokescreen'."
        },
        {
          "value": "deployed-as-a-penetration-test-or-user-awareness-training",
          "expanded": "Ransomware is very effective in the sense that most people know what its purpose is, and the dangers it may cause. As such, it is an excellent tool that can be used for demonstration purposes, such as a user awareness training. Another possibility is an external pentest, with same purpose."
        },
        {
          "value": "deployed-as-a-means-of-disruption-destruction",
          "expanded": "Last but not least -  while ransomware can have several purposes, it can also serve a particularly nasty goal: destroy a company or organisation, or at least take them offline for several days, or even weeks.\nAgain, there are some possibilities, but this may be a rivalry company in a similar business, again a disgruntled employee, or to disrupt large organisations on a worldwide scale."
        }
      ]
    },
    {
      "predicate": "target",
      "entry": [
        {
          "value": "pc-workstation",
          "expanded": "Ransomware that targets PCs or workstations."
        },
        {
          "value": "mobile-device",
          "expanded": "Ransomware that targets mobile devices."
        },
        {
          "value": "iot-cps-device",
          "expanded": "Ransomware that targets IoT or CPS devoces."
        },
        {
          "value": "end-user",
          "expanded": "Ransomware that targets end users."
        },
        {
          "value": "organisation",
          "expanded": "Ransomware that targets organisation."
        }
      ]
    },
    {
      "predicate": "infection",
      "entry": [
        {
          "value": "phishing-e=mails",
          "expanded": "Malicious e-mails are the most commonly used infection vectors for ransomware. Attackers send spam e-mails to victims that have attachments containing ransomware. Such spam campaigns can be distributed using botnets. Ransomware may come with an attached malicious file, or the e-mail may contain a malicious link that will trigger the installation of ransomware once visited (drive-by download)."
        },
        {
          "value": "sms-instant-message",
          "expanded": "SMS Messages or IMs are used frequently for mobile ransomware. In such kind of infections, attackers send SMS messages or IMs to the victims that will cause them to browse a malicious website to download ransomware to their platforms."
        },
        {
          "value": "malicious-apps",
          "expanded": "Malicious Applications are used by ransomware attackers who develop and deploy mobile applications that contain ransomware camouflaged as a benign application."
        },
        {
          "value": "drive-by-download",
          "expanded": "Drive-by download happens when a user unknowingly visits an infected website or clicks a malicious advertisement (i.e., malvertisement) and then the malware is downloaded and installed without the user’s knowledge."
        },
        {
          "value": "vulnerabilities",
          "expanded": "Vulnerabilities in the victim platform such as vulnerabilities in operating systems, browsers, or software can be used by ransomware authors as infection vectors. Attackers can use helper applications, exploit kits, to exploit the known or zero-day vulnerabilities in target systems. Attackers can redirect victims to those kits via malvertisement and malicious links."
        }
      ]
    },
    {
      "predicate": "communication",
      "entry": [
        {
          "value": "hard-coded-ip",
          "expanded": "Ransomware connecting to C&C via hard-coded IP addresses or domains"
        },
        {
          "value": "dga-based",
          "expanded": "Ransomware connecting to C&C via dynamically fast-fluxed/generated/shifted domain names using Domain Generation Algorithms (DGA)"
        }
      ]
    },
    {
      "predicate": "malicious-action",
      "entry": [
        {
          "value": "symmetric-key-encryption",
          "expanded": "Ransomware that encrypts data using symmetric-key encryption."
        },
        {
          "value": "asymmetric-key-encryption",
          "expanded": "Ransomware that encrypts data using asymmetric-key encryption."
        },
        {
          "value": "hybrid-key-encryption",
          "expanded": "Ransomware that encrypts data using hybrid-key encryption."
        },
        {
          "value": "screen-locking",
          "expanded": "Ransomware that locks the system’s graphical user interface and prevent access."
        },
        {
          "value": "browser-locking",
          "expanded": "Ransomware that locks slock web browser of the victim."
        },
        {
          "value": "mbr-locking",
          "expanded": "Ransomware that locks Master Boot Records."
        },
        {
          "value": "data-exfiltration",
          "expanded": "Ransomware that exfiltrates data."
        }
      ]
    }
  ]
}
```