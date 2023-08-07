from pyderivationagent.kg_operations.gateway import jpsBaseLibGW

### Create required JAVA classes ###

# Create ONE JVM module view and import the required classes
jpsBaseLibView = jpsBaseLibGW.createModuleView()
# jpsBaseLibGW.importPackages(jpsBaseLibView, "uk.ac.cam.cares.jps.base.agent.DerivationAgent")

# jpsBaseLibGW.importPackages(jpsBaseLibView, "uk.ac.cam.cares.jps.base.agent.*")
jpsBaseLibGW.importPackages(jpsBaseLibView, "uk.ac.cam.cares.jps.base.derivation.*")

# Obtain the relevant constants from Java side
print(str(jpsBaseLibView.JPSAgent.EMPTY_REQUEST_MSG))
# DERIVATION_AGENT_EMPTY_REQUEST_MSG = jpsBaseLibView.DerivationAgent.EMPTY_REQUEST_MSG
DERIVATION_CLIENT_AGENT_INPUT_KEY = jpsBaseLibView.DerivationClient.AGENT_INPUT_KEY
DERIVATION_CLIENT_AGENT_OUTPUT_KEY = jpsBaseLibView.DerivationClient.AGENT_OUTPUT_KEY
DERIVATION_CLIENT_DERIVATION_KEY = jpsBaseLibView.DerivationClient.DERIVATION_KEY
DERIVATION_CLIENT_SYNC_NEW_INFO_FLAG = jpsBaseLibView.DerivationClient.SYNC_NEW_INFO_FLAG
DERIVATION_CLIENT_AGENT_IRI_KEY = jpsBaseLibView.DerivationClient.AGENT_IRI_KEY
DERIVATION_CLIENT_DERIVATION_TYPE_KEY = jpsBaseLibView.DerivationClient.DERIVATION_TYPE_KEY
DERIVATION_CLIENT_BELONGSTO_KEY = jpsBaseLibView.DerivationClient.BELONGSTO_KEY
DERIVATION_CLIENT_DOWNSTREAMDERIVATION_KEY = jpsBaseLibView.DerivationClient.DOWNSTREAMDERIVATION_KEY
DERIVATION_SPARQL_ONTODERIVATION_DERIVATIONASYN = jpsBaseLibView.DerivationSparql.ONTODERIVATION_DERIVATIONASYN
DERIVATION_OURPUTS_RETRIEVED_INPUTS_TIMESTAMP_KEY = jpsBaseLibView.DerivationOutputs.RETRIEVED_INPUTS_TIMESTAMP_KEY
# print(str(DERIVATION_AGENT_EMPTY_REQUEST_MSG))
print(str(DERIVATION_CLIENT_AGENT_INPUT_KEY))
print(str(DERIVATION_CLIENT_AGENT_OUTPUT_KEY))
print(str(DERIVATION_CLIENT_DERIVATION_KEY))
print(str(DERIVATION_CLIENT_SYNC_NEW_INFO_FLAG))
print(str(DERIVATION_CLIENT_AGENT_IRI_KEY))
print(str(DERIVATION_CLIENT_DERIVATION_TYPE_KEY))
print(str(DERIVATION_CLIENT_BELONGSTO_KEY))
print(str(DERIVATION_CLIENT_DOWNSTREAMDERIVATION_KEY))
print(str(DERIVATION_SPARQL_ONTODERIVATION_DERIVATIONASYN))
print(str(DERIVATION_OURPUTS_RETRIEVED_INPUTS_TIMESTAMP_KEY))
print("Done")
