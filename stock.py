import yfinance as yf
import tweepy


#Keys and tokens are not shown for security reasons. With these users can gain access to my twitter.

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


client = tweepy.Client(
    bearer_token,
    api_key,
    api_key_secret,
    access_token,
    access_token_secret
)



tickersText = " MMM, AOS, ABT, ABBV, ACN, ATVI, ADM, ADBE, ADP, AES, AFL, A, APD, AKAM, ALK, ALB, ARE, ALGN, ALLE, LNT, ALL, GOOGL, GOOG, MO, AMZN, AMCR, AMD, AEE, AAL, AEP, AXP, AIG, AMT, AWK, AMP, AME, AMGN, APH, ADI, ANSS, AON, APA, AAPL, AMAT, APTV, ACGL, ANET, AJG, AIZ, T, ATO, ADSK, AZO, AVB, AVY, AXON, BKR, BALL, BAC, BBWI, BAX, BDX, WRB, BRK-B, BBY, BIO, TECH, BIIB, BLK, BK, BA, BKNG, BWA, BXP, BSX, BMY, AVGO, BR, BRO, BG, CHRW, CDNS, CZR, CPT, CPB, COF, CAH, KMX, CCL, CARR, CTLT, CAT, CBOE, CBRE, CDW, CE, COR, CNC, CNP, CDAY, CF, CRL, SCHW, CHTR, CVX, CMG, CB, CHD, CI, CINF, CTAS, CSCO, C, CFG, CLX, CME, CMS, KO, CTSH, CL, CMCSA, CMA, CAG, COP, ED, STZ, CEG, COO, CPRT, GLW, CTVA, CSGP, COST, CTRA, CCI, CSX, CMI, CVS, DHI, DHR, DRI, DVA, DE, DAL, XRAY, DVN, DXCM, FANG, DLR, DFS, DIS, DG, DLTR, D, DPZ, DOV, DOW, DTE, DUK, DD, DXC, EMN, ETN, EBAY, ECL, EIX, EW, EA, ELV, LLY, EMR, ENPH, ETR, EOG, EPAM, EQT, EFX, EQIX, EQR, ESS, EL, ETSY, EG, EVRG, ES, EXC, EXPE, EXPD, EXR, XOM, FFIV, FDS, FICO, FAST, FRT, FDX, FITB, FSLR, FE, FIS, FI, FLT, FMC, F, FTNT, FTV, FOXA, FOX, BEN, FCX, GRMN, IT, GEHC, GEN, GNRC, GD, GE, GIS, GM, GPC, GILD, GL, GPN, GS, HAL, HIG, HAS, HCA, PEAK, HSIC, HSY, HES, HPE, HLT, HOLX, HD, HON, HRL, HST, HWM, HPQ, HUM, HBAN, HII, IBM, IEX, IDXX, ITW, ILMN, INCY, IR, PODD, INTC, ICE, IFF, IP, IPG, INTU, ISRG, IVZ, INVH, IQV, IRM, JBHT, JKHY, J, JNJ, JCI, JPM, JNPR, K, KVUE, KDP, KEY, KEYS, KMB, KIM, KMI, KLAC, KHC, KR, LHX, LH, LRCX, LW, LVS, LDOS, LEN, LNC, LIN, LYV, LKQ, LMT, L, LOW, LYB, MTB, MRO, MPC, MKTX, MAR, MMC, MLM, MAS, MA, MTCH, MKC, MCD, MCK, MDT, MRK, META, MET, MTD, MGM, MCHP, MU, MSFT, MAA, MRNA, MHK, MOH, TAP, MDLZ, MPWR, MNST, MCO, MS, MOS, MSI, MSCI, NDAQ, NTAP, NFLX, NWL, NEM, NWSA, NWS, NEE, NKE, NI, NDSN, NSC, NTRS, NOC, NCLH, NRG, NUE, NVDA, NVR, NXPI, ORLY, OXY, ODFL, OMC, ON, OKE, ORCL, OGN, OTIS, PCAR, PKG, PANW, PARA, PH, PAYX, PAYC, PYPL, PNR, PEP, PFE, PCG, PM, PSX, PNW, PXD, PNC, POOL, PPG, PPL, PFG, PG, PGR, PLD, PRU, PEG, PTC, PSA, PHM, QRVO, PWR, QCOM, DGX, RL, RJF, RTX, O, REG, REGN, RF, RSG, RMD, RVTY, RHI, ROK, ROL, ROP, ROST, RCL, SPGI, CRM, SBAC, SLB, STX, SEE, SRE, NOW, SHW, SPG, SWKS, SJM, SNA, SEDG, SO, LUV, SWK, SBUX, STT, STLD, STE, SYK, SYF, SNPS, SYY, TMUS, TROW, TTWO, TPR, TRGP, TGT, TEL, TDY, TFX, TER, TSLA, TXN, TXT, TMO, TJX, TSCO, TT, TDG, TRV, TRMB, TFC, TYL, TSN, USB, UDR, ULTA, UNP, UAL, UPS, URI, UNH, UHS, VLO, VTR, VRSN, VRSK, VZ, VRTX, VFC, VTRS, VICI, V, VMC, WAB, WBA, WMT, WBD, WM, WAT, WEC, WFC, WELL, WST, WDC, WRK, WY, WHR, WMB, WTW, GWW, WYNN, XEL, XYL, YUM, ZBRA, ZBH, ZION, ZTS"

tickers = tickersText.replace(" ","").split(',')

maxPercentage = -100000
maxTicker = ""
for i in tickers:
    stock = yf.Ticker(i)

    history = stock.history(period="1da")

    openPrice = round(history['Open'][-1], 2)
    closePrice = round(history['Close'][-1], 2)

    percentage = ((closePrice - openPrice)/openPrice) * 100
    if percentage > maxPercentage:
        maxPercentage = percentage
        maxTicker = i

stock = yf.Ticker(maxTicker)

if stock.info['state'] is not None:
    text = (stock.info['shortName']+"("+maxTicker+")"+ " has had the highest increase today with a " + str(round(maxPercentage, 2)) + 
    "% increase. They are in the " +stock.info['industry']+" industry, and are based in " + stock.info['city'] + ","+stock.info['state']+". YAYAYA")
else:
    text = (stock.info['shortName']+"("+maxTicker+")"+ " has had the highest increase today with a " + str(round(maxPercentage, 2)) + 
    "% increase. They are in the " +stock.info['industry']+" industry, and are based in " + stock.info['city']+".")


client.create_tweet(text=text)

