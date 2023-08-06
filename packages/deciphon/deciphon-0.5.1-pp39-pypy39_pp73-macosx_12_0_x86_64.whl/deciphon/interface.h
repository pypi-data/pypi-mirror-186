struct dcp_press;

struct dcp_press *dcp_press_new(void);
int dcp_press_open(struct dcp_press *, char const *hmm, char const *db);
long dcp_press_nproteins(struct dcp_press const *);
int dcp_press_next(struct dcp_press *);
bool dcp_press_end(struct dcp_press const *);
int dcp_press_close(struct dcp_press *);
void dcp_press_del(struct dcp_press const *);

char const *dcp_strerror(int err);
